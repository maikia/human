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
def save_data(folder, file, data, scale, fs,record_type, traced, human, comments):
    """ it takes the given parameters of the data and saves it
    to the given file in the given folder. If the folder does not exist it
    will be created first"""
    fold.create_folder(folder)
    full_path = os.path.join(folder, file)
    
    np.savez(full_path, data = data, scale = scale, fs = fs,
             record_type=record_type, traced=traced, human=human, comments=comments)   


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


def save_data_as_npz(folder_data, file_data, folder_save, file_save,record_type, traced, human, comments):
    """ takes given data file from the data folder (.abf) and saves 
    it as .npz file under file_save in the folder_save"""
    
    fold.create_folder(folder_save)
    data, scale, fs = read_data(folder_data, file_data)   
    save_data(folder_save, file_save, data, scale, fs,record_type, traced, human, comments)
    del data, scale, fs

def calculate_spike_width(data, up = False):
    """ """
    # if spike is going up, change the whole data to the opposite direction
    if up:
        data = data * (-1.)
        
    # detect lowest point in the given range
    min_point_idx = np.argmin(data)
    before_min = np.diff(data[0:min_point_idx])
    before_min[before_min < 0] = 0
    before_min[before_min >0] = 1
    max_left_idx = np.where(before_min == 1)[0]
    
    if len(max_left_idx) == 0:
        max_left_idx = 0
    else: 
        max_left_idx = max_left_idx[-1]   
    
    after_min = np.diff(data[min_point_idx:])
    after_min[after_min < 0] = 0
    after_min[after_min > 0] = 1
    max_right_idx = np.where(after_min == 0)[0]
    
    if len(max_right_idx) == 0:
        max_right_idx = len(data)-1
    else: 
        max_right_idx = max_right_idx[0] + min_point_idx

    max_left = data[max_left_idx]
    max_right = data[max_right_idx]
    peak = data[min_point_idx]
    mid_high_point = np.mean([max_left, max_right])
    
    depth = np.abs(mid_high_point - peak)
    appear_time_pts = min_point_idx
    
    mid_hight = np.mean([mid_high_point, peak])
    # find on the left side at which index is mid hight

    left_mid_below = np.where((data[max_left_idx:min_point_idx] < mid_hight) == True)[0]
    if len(left_mid_below) == 0:
        left_mid_below = max_left_idx
    else:
        left_mid_below = left_mid_below[0] + max_left_idx

#        import pdb; pdb.set_trace()
    left_mid_above = left_mid_below-1
    
    # find on the right side at which index is mid hight

    right_mid_above = np.where((data[min_point_idx:max_right_idx] < mid_hight) == False)[0]
    if len(right_mid_above) == 0:
        right_mid_above = max_right_idx
    else:
        right_mid_above = right_mid_above[0] + min_point_idx
        
    right_mid_below = right_mid_above-1    
    
    #Calculate index of the midpoint (it most likely will be float)
    high_left = data[left_mid_above]
    low_left =  data[left_mid_below]
    exact_mid_left = left_mid_below - int((mid_hight - low_left)/(high_left - low_left) * 100)/100.0
    
    
    high_right = data[right_mid_above]
    low_right =  data[right_mid_below]
    exact_mid_right = right_mid_below + int((mid_hight - low_right)/(high_right - low_right)*100)/100.0
    
    mid_width_pts =   exact_mid_right-  exact_mid_left
    
    return appear_time_pts, mid_width_pts, depth

def calculate_spike_width_in_traces(folder_save,file2save_filtnpz, traces = [], time_range = [16.5,18.5], 
                                    electrode = 1, up = False):
    """ reads the data divided to traces, takes the range part from each 
    of the trace (unless range == [], than it takes the whole piece), and finds the parameters 
    of the spike or the wave (as in calculate_spike_width) and returns the params:
    width of the spike, exact ms when it's peak appears, it's depth 
    Parameter up says if spike is going up or down """
    [data, y_scale, fs] = read_npzdata(folder_save, file2save_filtnpz, "data", "scale", "fs")
    
    if traces != []:
        data = data[:,traces,:]
    
    if range != []:
        time_range_pts = [int(ms2pts(time_range[0], fs)),int(ms2pts(time_range[1], fs))]
        data = data[:,:,time_range_pts[0]:time_range_pts[1]]
        
    data = data[electrode, :,:]
    
    all_times = np.zeros(len(data))
    all_width = np.zeros(len(data))
    all_depth = np.zeros(len(data))
    
    for trace in range(len(data)):
        time_pts, width_pts, all_depth[trace] = calculate_spike_width(data[trace,:], up = up)
        all_times[trace] = pts2ms(time_pts, fs)
        all_width[trace] =pts2ms(width_pts, fs)
    
    del data
    return all_times + time_range[0], all_width, all_depth


def calculate_ratio_maxs_in_electrodes(folder_save,file_save, electrodes = [], 
                                       el1_max = True, el2_max = True, traces = [],
                                       remove_avg = False, plot_it = True, 
                                       title = 'ratio', x_range = [], y_range = [], 
                                       fig_type = '.png'):
    """ data must be divided to traces """
    [data, y_scale, fs] = read_npzdata(folder_save, file_save, "data", "scale", "fs")
    if traces != []:
        data = data[:, traces, :]
    data = data[electrodes,:,:]
    
    if remove_avg:
        for trace in range(np.size(data,1)):
            calc_avg = np.average(data[:,trace,0:100],1)
            data[:,trace,:]=data[:,trace,:]-np.transpose(np.resize(calc_avg,(len(data[0,0,:]),len(calc_avg))))
    
    el1 = data[electrodes[0],:,:]
    el2 = data[electrodes[1],:,:]

    if el1_max:
        max_el1 = np.max(el1,1)
    else:
        max_el1 = np.abs(np.min(el1,1))
    if el2_max:    
        max_el2 = np.max(el2,1)
    else:
        max_el2 = np.abs(np.min(el2,1))
    
    if plot_it:
        import pylab as plt
        plt.plot(max_el1, max_el2, 'o')
        
        
        if x_range != []:
            plt.xlim([x_range[0], x_range[1]])
    
        if y_range != []:
            plt.ylim([y_range[0], y_range[1]])
        plt.xlabel('electrode ' + str(electrodes[0]))
        plt.ylabel('electrode ' + str(electrodes[1]))
        plt.title(title)
        plt.savefig(folder_save+ title + fig_type)  
        plt.show()  

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
    [data, y_scale, fs,record_type, traced, human, comments] = read_npzdata(folder_data, file_data, "data", "scale", "fs", "record_type", "traced", "human", "comments")     
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
    save_data(new_folder, new_file, data, y_scale, fs,record_type, traced, human, comments)       
    


