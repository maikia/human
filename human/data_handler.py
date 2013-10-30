import numpy as np
import neo.io
import math
import os
import folder_handler as fold
import filtit as filt


####################- reading data - #
def read_data(folder, filename, segments = []):
    """ checks if the given file is correct, reads it and returns the data
    and the fs - sampling rate 
    folder - folder name
    filename - name of the file to read
    segments - don't fill if you want to read all of the segments, or if only
    one segment exists. otherwise use list to specify the numbers 
    of the segments, eg: (segment no 1 is first segment)
    segments = [1, 3, 4] 
    """
    # import pdb; pdb.set_trace()
    types_read = ['abf']
    
    # checks if this filetype can be read
    file_type = fold.check_type(filename)    
    if file_type not in types_read:
        raise Exception('Unable to read '+ file_type + ' files')
    
    # checks if given file exists
    full_path = os.path.join(folder, filename)
    fold.file_exists(full_path)
    
    if file_type == 'abf':
        data_list, no_segments = read_abfdata(full_path)

        # check if there is enough segments in the data
        if len(segments) > 0:
            if max(segments) > no_segments:
                raise Exception("Only " + str(no_segments) + " segments found")
        
        data, scale, fs = get_electrdata(data_list, no_segments, segments)  
    return data, scale, fs      


def read_abfdata(full_path):
    """ reads the .abf data and returns it as a list and number of 
    block segments in the data"""
    #import pdb; pdb.set_trace()
    
    print "Patience please, loading ", full_path, "...."
    
    reader = neo.io.AxonIO(filename=full_path)
    block = reader.read_block()
    data = []
    
    
    for i in range(len(block.segments)):
        seg = block.segments[i]
        data.append(seg.analogsignals)
    #import pdb; pdb.set_trace()
    return data, len(block.segments)

def get_electrdata(data, no_segments, segments = []):
    """ for given analogdata get the array of data for only one electrode and
    it's sampling rate
    segments - if [] all segments will be used, otherwise the ones which 
    are given, e.g. segments = [1, 3, 4]; fist segment is 1"""
    electr = []
    #import pdb; pdb.set_trace()
    
    if segments == []:
        segments = range(1, np.size(data, 1) + 1)
    
    dat = np.zeros((len(segments), no_segments, np.size(data,2)))

    scales = []
    
    for electr in segments:
        for trace in range(no_segments):
            el = electr - 1
            dat[el, trace, :] = data[trace][el].magnitude
            scales.append(str(data[trace][el].dimensionality))
            
    fs = data[0][0].sampling_rate
    fs = float(fs.magnitude)
    
    return dat, scales, fs

####################

def read_npzdata(folder, file, *arg):
    """ reads the given arg from given npz file """
    #import pdb; pdb.set_trace()
    full_path = os.path.join(folder, file)
    fold.file_exists(full_path)
    npz_data = np.load(full_path)
    
    parameters = []
    for param in arg:
        param_read = npz_data[param]
        parameters.append(param_read)
        
    del npz_data, param_read
    return parameters

###########################################################################

###########################saving data#####################################
def save_data(folder, file, data, scale, fs):
    """ it takes the given parameters of the data and saves it
    to the given file in the given folder. If the folder does not exist it
    will be created first"""
    fold.create_folder(folder)
    full_path = os.path.join(folder, file)
    
    np.savez(full_path, data = data, scale = scale, fs = fs)   


################# defining parameters in the data #####################
def get_timeline(data, fs, scale='ms'):
    """ returns the timeline of the given data 
    in prefered scale: 'sec', 'min' or 'ms' """
    divider = {'min': 1.0 / 60,
               'sec': 1.0,
               'ms' : 1000,
               }
    t = len(data) / fs * divider[scale]
    return np.linspace(0, t, len(data))

def ms2pts(ms, fs):
    """ converts number of ms to number of data pts"""
    pts = (fs / 1000.0) * ms
    return pts

def pts2ms(pts, fs):
    """ converts number of pts to number of ms"""
    ms = (pts/fs)*1000.0
    return ms


def save_data_as_npz(folder_data, file_data, folder_save, file_save):
    """ takes given data file from the data folder (.abf) and saves 
    it as .npz file under file_save in the folder_save"""
    
    fold.create_folder(folder_save)
    data, scale, fs = read_data(folder_data, file_data)   
    save_data(folder_save, file_save, data, scale, fs)
    del data, scale, fs

def trigger_on_spike(folder, file, new_folder_save, new_file_save, thresh = -30, el=0,
                     time_range=[-10,30], use_time = [], up = True, center_on_peak = False):
    """ reads gap free data from .npz file and triggers on event on given electrode 
    then it saves the new data in the form of the traces in .npz format"""
    [data, y_scale, fs] = read_npzdata(folder, file, "data", "scale", "fs")
    if use_time != []:
        data = data[:,:,use_time[0]:use_time[1]]
        
    # read the data from the given electrode
    data2trigger = data[el,0,:]
    time_range_pts = [int(ms2pts(time_range[0], fs)),int(ms2pts(time_range[1], fs))]
    
    # check which parts of the data are above the threshold
    if up:
        above_thres = [data2trigger >= thresh]
    else:
        above_thres = [data2trigger <= thresh]
        
    data_bool = data2trigger.copy()
    data_bool[above_thres[0]] = 1
    data_bool[~above_thres[0]] = 0
    
    # use the data with the margins cut to time_range given
    cut_margins = data_bool[-time_range_pts[0]:-time_range_pts[1]]
    
    last_id = -time_range_pts[0]
    next_id = np.where(cut_margins==1)[0]
    

    new_data=[]
    while len(next_id) > 0:
        # id where the next rise of the spike was found
        next_id = next_id[0]
        trig_id = next_id+last_id+1 # 
        new_trace = data[:,0,trig_id + time_range_pts[0]:trig_id + time_range_pts[1]]
        
        if center_on_peak:
            if up:
                move_pts = np.argmax(new_trace[el,time_range_pts[0]-1:])
            else:
                move_pts = np.argmin(new_trace[el,time_range_pts[0]-1:]) 
                
            trig_id = trig_id + move_pts
            new_trace = data[:,0,trig_id + time_range_pts[0]:trig_id + time_range_pts[1]]
        #if len(new_data) == 447:
            #import pdb; pdb.set_trace()
        new_data.append(new_trace)

        cut_margins = data_bool[trig_id +time_range_pts[1]:-time_range_pts[1]]
        last_id = trig_id + time_range_pts[1]
        next_id = np.where(cut_margins==1)[0]
        
    
    
    new_data = np.array(new_data)
    new_data = np.swapaxes(new_data,1,0)
    fold.create_folder(new_folder_save)  
    save_data(new_folder_save, new_file_save, new_data, y_scale, fs)
    del new_data, data, y_scale, fs 
    
def filter_data(folder_data, file_data, new_folder, new_file, freq, 
                electrodes = [],N = 100, filter_type = 'low_pass'):
    """ given the .npz file with the data, it filters the electrodes given
    and saves the new data in the new .npz file
    if electrodes == [], all electrodes will be used;
    N - filter order
    filter type = 'low_pass' or 'high_pass' or 'band_pass' """
    # extract the data
    [data, y_scale, fs] = read_npzdata(folder_data, file_data, "data", "scale", "fs")     
    if electrodes == []:
        electrodes = range(len(data))
    #import pdb; pdb.set_trace()
    #new_data = data.copy()
    
    freq= freq*(1.)
    for electr in electrodes:
        for trace in range(np.size(data,1)):
            # filter the data
            if filter_type == 'low_pass':
                b_lp = filt.FilterDesign((0, freq / fs), N) # < freq Hz
                data[electr,trace,:] = filt.filtfilt(b_lp, [1], data[electr,trace,:])        
            elif filter_type == 'high_pass':
                b_hp = filt.FilterDesign(( freq/ fs, 1), N) # > freq Hz
                data[electr,trace,:] = filt.filtfilt(b_hp, [1], data[electr,trace,:])        
            elif filter_type == 'band_pass':
                b_bp = filt.FilterDesign((freq[0] / fs, freq[1] / fs), N) # freq[0]Hz > x > freq[1]Hz
                data[electr,trace,:] = filt.filtfilt(b_bp, [1], data[electr,trace,:]) 
    
    
    fold.create_folder(new_folder)  
    save_data(new_folder, new_file, data, y_scale, fs)       
    
    
   
    
# - unfinished - untested
    


