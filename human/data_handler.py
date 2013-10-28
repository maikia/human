import numpy as np
import neo.io
import math
import os
import folder_handler as fold


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
    
# - unfinished - untested
    


