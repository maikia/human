import data_handler as dh
import folder_handler as fh
import display as display
import pylab as plt
import numpy as np

def get_figure_data_settings(fig_no = 1):
    """ here are saved all the parameters used for each figures 
    traced - say if the data is saved in traces (True) or in 'gap free' mode (False)"""
    data_folder = '/home/maja/PhDProject/data/'
    save_folder = '/home/maja/PhDProject/data/results/' 
    
    if fig_no == 0:
        specific_folder = 'HT2013_04_02'
        data_file = '2013_04_02_0013'
        record_type = '_DC_seizure'
        traced = False
    elif fig_no == 1:
        specific_folder = '2013_06_17'
        data_file = '2013_06_17_0007'
        record_type = '_seizure'
    elif fig_no == 2:
        specific_folder = '2013_09_03'
        data_file = '2013_09_03_0001'
        record_type = '_IPSP'
    elif fig_no == 3:
        specific_folder = '2013_09_03'
        data_file = '2013_09_03_0007'      
        record_type = '_noIPSP'  
    elif fig_no == 4.1:
        specific_folder = '2013_09_05'
        data_file = '2013_09_05_0016'   # try also: '05_09_2013_0017.abf'
        record_type = '_smallGABAb'
    elif fig_no == 4.2:
        specific_folder = '2013_09_05'
        data_file = '2013_09_05_0017'   # try also: '05_09_2013_0017.abf'
        record_type = '_smallGABAb'
    elif fig_no == 5:
        specific_folder = '2013_09_05'
        data_file = '2013_09_05_0020'  
        record_type =  '_largeGABAb'
    elif fig_no == 6:
        specific_folder = '2013_09_12'
        data_file = '2013_09_12_0000'   
        record_type =  '_synchEvents'
    elif fig_no == 6.1:
        specific_folder = '2013_09_12'
        data_file = '2013_09_12_0001'   
        record_type =  '_synchEvents2'
    elif fig_no == 7:
        specific_folder = '2013_09_27'
        data_file = '2013_09_27_0011' 
        record_type =  '_GABAb' 
    elif fig_no == 8:
        specific_folder = 'HT2013_09_24'
        data_file = '2013_09_24_0008' 
        record_type =  '_interictal' 
    elif fig_no == 9:
        specific_folder = 'HT2013_09_24'
        data_file = '2013_09_24_0013'   
        record_type =  '_seizures'
    elif fig_no == 10:
        specific_folder = '2013_10_01'
        data_file = '2013_10_01_0004'  
        record_type =  '_EIPSP'         
    elif fig_no == 11:
        specific_folder = '2013_08_10'
        data_file = '2013_10_08_0002' 
        record_type =  '_noNBAQ' 
    elif fig_no == 12:
        specific_folder = '2013_08_10'
        data_file = '2013_10_08_0008'  
        record_type =  '_NBAQ'
    elif fig_no == 13:
        specific_folder = 'HT2013_10_11'
        data_file = '2013_10_11_0010'  
        record_type =  '_synchrony'
    elif fig_no == 14:
        specific_folder = 'HT2013_10_11'
        data_file = '2013_10_11_0011'  
        record_type =  '_synchrony'
    elif fig_no == 15:
        specific_folder = '2013_10_16'
        data_file = '2013_10_16_0007'  
        record_type =  '_EPSP'
    elif fig_no == 15.1:
        specific_folder = '2013_10_16'
        data_file = '2013_10_16_0006'  
        record_type =  '_noEPSP'
    elif fig_no == 16:
        specific_folder = '2013_10_21'
        data_file = '2013_10_21_0004'  
        record_type =  '_EPSP'      
    elif fig_no == 17:
        specific_folder = '2013_10_21'
        data_file = '2013_10_21_0004'  
        record_type =  '_synchrony'
    elif fig_no == 18:
        specific_folder = '2013_10_21'
        data_file = '2013_10_21_0005'  
        record_type =  '_EPSP'
    elif fig_no == 19:
        specific_folder = '2013_10_21'
        data_file = '2013_10_21_0007'  
        record_type =  '_synchrony'
    elif fig_no == 20:
        specific_folder = 'HT2013_11_07'
        data_file = '2013_11_07_0001'
        record_type = '_interictal'
    elif fig_no == 21:
        specific_folder = 'HT2013_11_07'
        data_file = '2013_11_07_0002'
        record_type = '_activity_stoped'
    elif fig_no == 22:
        specific_folder = 'HT2013_11_07'
        data_file = '2013_11_07_0004'
        record_type = '_exc_synchrony10'
    elif fig_no == 23:
        specific_folder = 'HT2013_11_07'
        data_file = '2013_11_07_0007'
        record_type = '_exc_synchrony12'
    elif fig_no == 24:
        specific_folder = 'HT2013_11_07'
        data_file = '2013_11_07_0011'
        record_type = '_synch_blocked'
    elif fig_no == 25:
        specific_folder = '2013_11_22'
        data_file = '2013_11_22_0008' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_exc_synchrony' 
    elif fig_no == 26:
        specific_folder = '2013_12_04'
        data_file = '2013_12_04_0003' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_GABAa_synchrony1'         
    elif fig_no == 27:
        specific_folder = '2013_12_04'
        data_file = '2013_12_04_0009' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_GABAa_synchrony2'               
    elif fig_no == 28:
        specific_folder = '2014_04_02'
        data_file = '2014_04_02_0001' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_highCa' 
    elif fig_no == 29:
        specific_folder = '2014_04_02'
        data_file = '2014_04_02_0004' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx' 
    elif fig_no == 30:
        specific_folder = '2014_04_02'
        data_file = '2014_04_02_0005' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx'     
    elif fig_no == 31:
        specific_folder = '2014_04_02'
        data_file = '2014_04_02_0008' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_highCa' 
    elif fig_no == 32:
        specific_folder = '2014_04_02'
        data_file = '2014_04_02_0009' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx' 
    elif fig_no == 33:
        specific_folder = '2014_04_03'
        data_file = '2014_04_03_0000' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx' 
    elif fig_no == 34:
        specific_folder = '2014_04_03'
        data_file = '2014_04_03_0001' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx'  
    elif fig_no == 35:
        specific_folder = '2014_04_03'
        data_file = '2014_04_03_0003' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx' 
    elif fig_no == 36:
        specific_folder = '2014_04_03'
        data_file = '2014_04_03_0004' # '2013_11_07_0012' '2013_11_07_0013'
        record_type = '_CA_Ptx'  


    file_save = 'fig' + str(fig_no) + '_' + data_file + record_type + '.npz'            
    return data_folder, save_folder, specific_folder, data_file + '.abf', file_save #, traced


def create_json_file(fig_no):
    pass


def gather_data_info(fig_no):
    
    data_folder, save_folder, specific_folder, data_file, file_save, traced = get_figure_data_settings(fig_no=fig_no)
    folder_save = save_folder + specific_folder + '_results/'
    
    return data_folder, data_file, file_save, traced, folder_save
    

def analyze_data(fig_no, fig_type='.png',save_traces=False,show_traces=False,
                 time_type='ms',time_range=[],y_range=[],
                 plot_all_data=False,save_all_data_plot=False,
                 thres=1.0, el=0, up=True, center_on_peak=False,
                 time_range_all_data=[],time_range_select_traces=[-25000,60000]):
    """ analysis the data given by fig_no as specified by:
    fig_type - in which format the figures are going to be saved
    save_traces - should the traces be saved (True/False)
    show_traces - no matter if data is traced or not, 
        it can be separated to traces, and they can be displayed individually
    time_type - can be set to 'ms', 'sec' or 'min'
    time_range - if not set, all data range will be used
    y_range - if not set min to max of each trace will be used (each plot may end up having different y_range)
    electrodes - if not set, all the electrodes will be displayed
    y_range_intra - might be set differently than for the extracellular electrodes
    
    thres - set it if you want the data to be traced. On which threshold it should be triggered
    el - set on which electrode it should be triggered
    up - set True if you want it to be set on rising data, set False if on falling data
    center_on_peak - set True if you want the data to be set on the peak of triggered event, set False 
        if you want it to be aligned on the triggered place 
    
    plot_all_data - if the whole data, no matter if it's traced or not should be displayed
    save_all_data_plot - if the whole data, no matter if it's traced or not should be plotted and saved
    time_range_all_data - the whole data will use this parameter for displaying time_range of data [ms]
    time_range_select_traces - it uses this time range to select the traces from triggered event
    """
    
    # get the info of this figure
    data_folder, data_file, file_save, traced, folder_save = gather_data_info(fig_no)
    
    if plot_all_data or save_all_data_plot:
        save_file = 'whole_data' + fig_type
        display.plot_data(folder_save,save_file,folder_save,file_save,x_scale=time_type,
                          title = 'Data',time_range=time_range_all_data,y_range=y_range,
                          electrodes = [],y_range_intra = [],show_plot=plot_all_data,
                          save_plot=save_all_data_plot)        
    
    if (not traced) and (save_traces or show_traces):
        # divide the data to traces, it must be done only if the recording was gap free but 
        # and no point of doing it if it was saved in the trace format already
        # unless the parameters change now
        save_file = 'traced_data' + fig_type
        save_file_npz = 'fig_' + str(fig_no) + '.npz'
        dh.trigger_on_spike(folder_save, file_save, folder_save, save_file_npz, thresh = -1.1, el=0,
                     time_range=time_range_select_traces, up=up, center_on_peak=center_on_peak)
        
        display.plot_data(folder_save,save_file,folder_save,save_file_npz,x_scale=time_type,
                          title = 'Data',time_range=time_range,y_range=y_range,
                          electrodes = [],y_range_intra = [],show_plot=show_traces,save_plot=save_traces)
        
    if True:
        display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'interictal events', sweeps = [0,1,2],
                               electrodes = [0,1,2,3], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
        import pdb; pdb.set_trace()
     

def figure_exp_0(fig_type = '.png',save_traces=False, show_traces = True):
    """ DC shift in human"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 0)
    file2save_npz = 'fig0_' + '.npz'
    
    file2save = 'DC_seizures' + fig_type
    file2save_example = 'egDC_seizures' + fig_type
    folder_save = save_folder + specific_folder + '_results/'
    y_range = [-200,200]
    #display.plot_data(folder_save, file2save_example,folder_save,file_save,x_scale = 'sec', 
    #             y_range=y_range, time_range = [90000,160000], electrodes=[],
    #             y_range_intra = [-2,0]) 

    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        
        #dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -1.1, el=0,
        #             time_range=[-25000,60000], up = False, center_on_peak = False)
        
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [0,1,2,3],y_range =y_range)
        #import pdb; pdb.set_trace() 

    time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    file_save = 'DC_shift_all' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'interictal events', sweeps = [0,1,2],
                               electrodes = [0,1,2,3], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_1(fig_type = '.png'):
    """ seizure-like activity from human """
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 1)
    folder_save = save_folder + specific_folder + '_results/'
    
    # plot trace of few waves
    file2save = 'seizure_like' + fig_type
    tit = 'seizure like activity in human subiculum'
    time_range = [140000,180000]# in ms
    y_range = [-100,100]
    display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms',
                      title=tit,time_range=time_range,y_range = y_range)
    
    # plot only one wave
    file2save = 'one_wave' + fig_type
    tit = 'seizure like activity in human subiculum'
    time_range = [149900,151500]# in ms
    y_range = [-100,100]
    display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms',
                      title=tit,time_range=time_range,y_range = y_range)   
    
def figure_exp_2(fig_type = '.png', save_traces = False, show_traces = False):
    """ nothing added to the solution, cell induces IPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 2)
    folder_save = save_folder + specific_folder + '_results/'
    file2save_npz = 'fig2_' + '.npz'
    file2save_filtnpz = 'fig2_filt_' + '.npz'
    file2save = 'fig2_' + fig_type
    
    filt_for_fig = 'high_pass2.npz'
    dh.filter_data(folder_save, file_save, folder_save, filt_for_fig, 2.0, 
       electrodes = [2],N = 100, filter_type = 'high_pass')
    display.plot_data(folder_save,file2save,folder_save,filt_for_fig,x_scale = 'ms', time_range = [4050,4800],electrodes=[2])
    
    if save_traces:
        """ it must be done only if the recording was gap free but 
        it was not saved in the trace format yet"""

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        new_file = 'filtered_data_above500.npz'
        #dh.filter_data(folder_save, file_save, folder_save, new_file, 500.0, 
        #        electrodes = [2],N = 100, filter_type = 'high_pass')
        
        #dh.trigger_on_spike(folder_save, new_file, folder_save, file2save_filtnpz, thresh = -30, el=0,
        #             time_range=[-15,50])
        
        #display.plot_data(folder_save,file2save,folder_save,file2save_filtnpz,
        #                  x_scale = 'ms', y_range = [-20,20],electrodes = [0,2])
        #                  #time_range = [15,23])
        
        all_times1, all_width1, all_depth1 = dh.calculate_spike_width_in_traces(folder_save,
                                            file2save_filtnpz, traces = [2, 5, 9, 13, 16, 17, 18, 21], time_range = [16.9,18.7])
        all_times2, all_width2, all_depth2 = dh.calculate_spike_width_in_traces(folder_save,
                                            file2save_filtnpz, traces = [6, 19, 48, 73, 88, 103, 110, 119, 126], time_range = [19.0,22.0])
        
        print 'half width of spike 1 (calculated on some traces): ' + str(np.mean(all_width1)) + ' ms'
        print 'depth of spike 1 (calculated on some traces): ' + str(np.mean(all_depth1)) + ' ms'
        print 'half width of spike 2 (calculated on some traces): ' + str(np.mean(all_width2)) + ' ms'
        print 'depth of spike 2 (calculated on some traces): ' + str(np.mean(all_depth2)) + ' ms'        

    file_save = 'IPSP_traces2_' + fig_type
    time_range = [5,40] # in ms
    y_range = [-20, 35]
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'normal ringer', sweeps = [60, 66, 72, 86, 91], #, 51, 57, 66, 67, 72, 77, 86, 91, 113, 122, 128], #[8,25, 29,32,33],
                               electrodes = [0,2], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    
    file_save = 'IPSP_spike2_' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'normal ringer', sweeps = [23, 26, 62, 89, 100], #, 17, 18, 26, 39, 45, 49, 53, 62, 71, 84, 89, 100, 103, 108, 124],#[4,10, 11, 14, 18],
                               electrodes = [0,2], y_range = y_range, time_range = time_range,
                              remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_3(fig_type = '.png', save_traces = False, show_traces = False): 
    """ NBQX was added to the solution, cell induces IPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 3)
    folder_save = save_folder + specific_folder + '_results/'
    file2save_npz = 'fig3_' + '.npz'
    file2save = 'fig3_' + fig_type
    
    if save_traces:
        """ it must be done only if the recording was gap free but 
        it was not saved in the trace format yet"""
        

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -30, el=0,
                     time_range=[-15,50])
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms')
        
    file_save = 'after_NBQX' + fig_type
    time_range = [5,40] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'NBQX added', sweeps = [4, 5, 7, 10, 12],
                               electrodes = [0,2], y_range = [-20, 35], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()       
    
def figure_exp_4_1(fig_type = '.png', save_traces = False, show_traces = False):
    """ small GABAb events"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 4.1)
    folder_save = save_folder + specific_folder + '_results/'
    file2save_npz = 'fig3_' + '.npz'
    file2save = 'part_of_trace_16' + fig_type
    
    if save_traces:
        """ it must be done only if the recording was gap free but 
        it was not saved in the trace format yet"""
        

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        #dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -88, el=0,
        #             time_range=[-600,600], use_time=[25000,-1], up = False, center_on_peak = True)
        #display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms',y_range =[-70, 70])
        # 
    #dh.calculate_ratio_maxs_in_electrodes(folder_save,file2save_npz, electrodes = [0,1],remove_avg = True,
    #                                         el1_max = False, el2_max = True, x_range = [0,26], y_range = [5,60], 
    #                                         traces = [1,2,4,5,6,7,8,9,10,12, 13, 14, 15, 16, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 35, 36],
    #                                         title = 'ratio_4_1', fig_type = fig_type)
        
    display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'sec', time_range=[52000,64000], 
                      electrodes = [0,1,2])
    
    different_events = [[1,23], [2, 6, 12, 20, 28], [10, 22, 25, 30],[27,15,26],
                       [7,8], [4,5,9,13,14], [27,15,26]]
    files_save = ["small_GABAb_I", "small_GABAb_II", "small_GABAb_III", "small_GABAb_IV",
                 "small_GABAb_V", "small_GABAb_VI", "others"] 
    titles = ["GABAb events type I, 2 waves", "GABAb events type II, 5 waves",
              "GABAb events type III, 4 waves","GABAb events type IV, 3 waves",
              "GABAb events type V, 2 waves","GABAb events type VI, 5 waves", 
              "others"]
    
    time_range = [0,1200] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    
    for next_id in range(len(different_events)):

        file_save = files_save[next_id] + fig_type

        #import pdb; pdb.set_trace()
        display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = titles[next_id], sweeps = different_events[next_id],
                               electrodes = [0,1,2], y_range = [-20, 45], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()     
    
def figure_exp_4_2(fig_type = '.png', save_traces = False, show_traces = False):
    """ small GABAb events"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 4.2)
    folder_save = save_folder + specific_folder + '_results/'
    file2save_npz = 'fig4_' + '.npz'
    file2save = 'part_of_trace_17' + fig_type
    

    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -88, el=0,
                     time_range=[-600,600], use_time=[25000,-1], up = False, center_on_peak = True)
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms',y_range =[-400, 400])
        
    dh.calculate_ratio_maxs_in_electrodes(folder_save,file2save_npz, electrodes = [0,1],el1_max = False, el2_max = True,
                    remove_avg = True,x_range = [0,26], y_range = [5,60], 
                    traces = [1,2,3,4,5,6,7,8,9,11,12,13,14,16],
                    title = 'ratio_4_2', fig_type = fig_type)
   
    display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'sec', time_range=[140000,160000], 
                      electrodes = [0,1,2], y_range=[-500,500])
    
    different_events = [[10,17], [1,4, 5, 6],[2,3,7,8,9,11,12,13,14,16]]
    files_save = ["synch_I", "synch_II", "synch_III"] 
    titles = ["synch I, 2 events", "synch II, 4 events", "synch III, 10 events"]
    y_ranges = [[-500,1200],[-300,800],[-100,100]]
    
    time_range = [0,1200] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    
    for next_id in range(len(different_events)):

        file_save = files_save[next_id] + fig_type

        #import pdb; pdb.set_trace()
        display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = titles[next_id], sweeps = different_events[next_id],
                               electrodes = [0,1,2], y_range = y_ranges[next_id], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()       

def figure_exp_5(fig_type = '.png',show_traces = False):
    """ large GABAb events, triggered"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 5)
    folder_save = save_folder + specific_folder + '_results/'

    fig_save = 'large_synch_20' + fig_type
    time_range = [50,400] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    display.plot_data_one_mean(data_details, folder_save, fig_save, x_scale = 'ms',
                               title = 'large Gabab synchronised events', sweeps = [0, 2,3,4,7,8],
                               electrodes = [0,1,2], y_range = [-500,1200], time_range = time_range,
                               remove_avg = True) 
    
    if show_traces:
        plt.show()
   
def figure_exp_6(fig_type = '.png', save_traces = False,show_traces = False):
    """ large GABAb events, triggered"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 6)
    file2save_npz = 'fig6_' + '.npz'
    file2save = 'part_of_trace' + fig_type
    
    folder_save = save_folder + specific_folder + '_results/'
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #                 electrodes = [0,2,3], y_range=[-1000,1000])
    
    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -500, el=2,
                     time_range=[-300,1500], up = False, center_on_peak = False)
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [0,2,3],y_range =[-300, 1500])
   
    
    fig_save = 'large_synch_20' + fig_type
    #time_range = [50,400] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    display.plot_data_one_mean(data_details, folder_save, fig_save, x_scale = 'ms',
                               title = 'large Gabaa synchronised events', sweeps = [0, 1,2,4,5,6],
                               y_range_intra = [-10, 20], electrodes = [0,2,3], y_range = [-1000,1000],
                               remove_avg = True) 
    if show_traces:
        plt.show()


def figure_exp_6_1(fig_type = '.png', save_traces = False,show_traces = False):
    """ large GABAb events, triggered"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 6.1)
    file2save_npz = 'fig6_1_' + '.npz'
    file2save = 'part_of_trace' + fig_type
    
    folder_save = save_folder + specific_folder + '_results/'
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #                 electrodes = [0,2,3], y_range=[-1000,1000])
    
    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -500, el=2,
                     time_range=[-300,1500], up = False, center_on_peak = False)
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [0,2,3],y_range =[-300, 1500])
   
    
    fig_save = 'large_synch_2' + fig_type
    time_range = [0,800] # in ms

    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    display.plot_data_one_mean(data_details, folder_save, fig_save, x_scale = 'ms',
                               title = 'large Gabaa synchronised events', sweeps = [8, 6, 7,9,10],
                               y_range_intra = [-10, 20], electrodes = [0,2], y_range = [-1000,1000],
                               remove_avg = True, time_range = time_range) 
    if show_traces:
        plt.show()


def figure_exp_7(fig_type = '.png', save_traces = False,show_traces = False):
    """ large GABAb events, triggered"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 7)
    file2save_npz = 'fig6_' + '.npz'
    file2save = 'part_of_trace' + fig_type
    
    folder_save = save_folder + specific_folder + '_results/'
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #             electrodes = [1,2,3], y_range=[-1000,1000])
    
    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        # if aligned on the second electrode:
        #dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -100, el=2,
        #             time_range=[-600,600], up = False, center_on_peak = True)
        
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [0,1,2,3],y_range =[-1000, 1000])
   
    
    different_events = [[1,4,5,7,16], [9,10],[2,6,8]]
    files_save = ["synch_I", "synch_II", "synch_III"] 
    titles = ["synch I, 6 events", "synch II, 2 events", "synch III, 3 events"]
    #y_ranges = [[-500,1200],[-300,800],[-100,100]]
    
    time_range = [0,1500] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    
    y_range = [] #[-500,500]
    
    for next_id in range(len(different_events)):

        file_save = files_save[next_id] + fig_type

        #import pdb; pdb.set_trace()
        display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = titles[next_id], sweeps = different_events[next_id],
                               electrodes = [0,1,2,3], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_8(fig_type = '.png', save_traces = False):
    """ large GABAb events, triggered"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 8)
    file2save_npz = 'fig8_' + '.npz'
    file2save = 'part_of_trace' + fig_type
    
    folder_save = save_folder + specific_folder + '_results/'
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #             electrodes = [1,2,3], y_range=[-100,100])

    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -30, el=2,
                     time_range=[-200,200], up = False, center_on_peak = True)
        #display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
        #                  electrodes = [1,2,3],y_range =[-100, 100])


    time_range = [100,400] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    file_save = 'interictal' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'interictal events', sweeps = [0,1,2,3,4,5,6],
                               electrodes = [1,2,3], y_range = [-100,100], time_range = time_range,
                               remove_avg = True) 
    plt.show()

def figure_exp_9(fig_type = '.png', save_traces = False,show_traces = True):
    """ seizures"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 9)
    file2save_npz = 'fig9_' + '.npz'
    file2save = 'seizure_1' + fig_type
    file2save2 = 'seizure_2' + fig_type
    folder_save = save_folder + specific_folder + '_results/'
    
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 electrodes = [1, 2, 3], y_range=[], time_range = [235000, 340000]) 

    display.plot_data(folder_save, file2save2,folder_save,file_save,x_scale = 'sec', 
                 electrodes = [1, 2, 3], y_range=[], time_range = [520000, 610000]) 
        
    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -150, el=2,
                     time_range=[-200,200], up = False, center_on_peak = True)
        #display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
        #                  electrodes = [1,2,3],y_range =[-100, 100])


    time_range = [100,400] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    file_save = 'seizure' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'seizure events', sweeps = [0,1,2,3,4,5,6],
                               electrodes = [1,2,3], y_range = [], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()
 
def figure_exp_10(fig_type = '.png'):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 10)
    folder_save = save_folder + specific_folder + '_results/'
    #display.plot_data(folder_save, file_save, x_scale = 'ms')
    
    time_range = [35,70] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    
    file_save = 'NBQX_traces' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'after adding PTX', sweeps = [1,3, 5, 10],
                               electrodes = [0,1,3], y_range = [-20, 35], time_range = time_range) 
    plt.show()
    
    
def figure_exp_11(fig_type = '.png', show_traces = False):
    """ """
    IPSP_traces_all = [0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 23, 25, 26, 29, 35, # number: 68
                   37, 42, 44, 45, 47, 48, 49, 53, 54, 55, 65, 66, 69, 83, 85, 87, 90, 91, 100, 
                   103, 105, 106, 109, 110, 112, 113, 116, 118, 126, 131, 134, 143, 144, 149, 158, 
                   159, 160, 163, 164, 167, 168, 173, 174, 180, 183, 184, 185]
    no_IPSP_traces_all = [1, 3, 15, 24, 31, 36, 40, 50, 52, 56, 58, 60, 68, 70, 72, 73, 84, 88, 92, # number: 43
                      94, 97, 102, 104, 107, 111, 114, 120, 124, 125, 129, 132, 135, 136, 138, 
                      141, 142, 145, 154, 169, 170, 181, 182, 187]
    # number of all traces: 188 (traces not accounted above were more complex

    
    IPSP_traces_selected = [8, 16, 12, 4,16] #IPSP_traces_all[5:8] #[0, 2, 4, 5, 6]
    no_IPSP_traces_selected = [40, 30, 72, 33, 70] #[15, 24, 30, 1,3] #no_IPSP_traces_all[10:14] #[1, 3, 15, 24, 31]
    noise_traces = range(187)
    noise_traces = [x for x in noise_traces if (x not in IPSP_traces_selected) and (x not in no_IPSP_traces_selected)]
    
    time_range = [35, 65] # in ms
    
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 11)
    
    folder_save_fig = save_folder + specific_folder + '_results/'
    
    folder_save = save_folder + specific_folder + '_results/'
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    #import pdb; pdb.set_trace()     

    # plot every trace
    #display.plot_data(folder_save_fig,file_save + fig_type,folder_save,file_save,x_scale = 'ms', 
    #                  electrodes = [0,1,2],y_range =[-100, 100], time_range =time_range)
    
    
    file_save = 'IPSP_traces' + fig_type
    display.plot_data_one_mean(data_details,folder_save_fig, file_save, x_scale = 'ms', 
                               title = 'traces with IPSP',sweeps=IPSP_traces_selected,
                               electrodes = [0,1,2], time_range = time_range,
                               remove_avg = True) 
    file_save = 'no_IPSP_traces' + fig_type
    display.plot_data_one_mean(data_details,folder_save, file_save, x_scale = 'ms',
                               title = 'traces with no IPSP', 
                               sweeps=no_IPSP_traces_selected,
                               electrodes = [0,1,2], time_range = time_range,
                               remove_avg = True) 
    del data_details, temp
    if show_traces:
        plt.show()

def figure_exp_12(fig_type = '.png', show_traces = False):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 12)
    folder_save = save_folder + specific_folder + '_results/'
    
    time_range = [35, 65] # in ms
    
    import pdb; pdb.set_trace()  
    
    # plot every trace
    #display.plot_data(folder_save,file_save + fig_type,folder_save,file_save,x_scale = 'ms', 
    #                  electrodes = [0,1,2],y_range =[-100, 100], time_range =time_range)
    
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    
    file_save = 'NBQX_traces' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'after adding PTX', sweeps = [1,2,3,4,5],
                               electrodes = [0,1,2], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_13(fig_type = '.png', save_traces = False):
    """ seizures"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 13)
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'piece_of_trace' + fig_type
    time_range = [13000, 38000] # in ms
    display.plot_data(folder_save, file2save, folder_save, file_save,x_scale = 'sec', 
                      time_range = time_range,electrodes = [0,2,3])     
    
                                
    

def figure_exp_14(fig_type = '.png',show_traces = True):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 14)
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'synchrony_' + fig_type
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec')     
    
    #time_range = [35, 65] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    
    file_save = 'synch_events' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'NBQX, 4AP, human subiculum, 10 events', 
                               sweeps = [1,2,3,4,7,9,10,12,27,32],
                               electrodes = [0,2,3],remove_avg = True, y_range = [-100, 100]) 
    if show_traces:
        plt.show()
    
    
    
def figure_exp_15(fig_type = '.png', show_traces = False):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 15)
    folder_save = save_folder + specific_folder + '_results/'
    
    #display.plot_data(folder_save, file_save, x_scale = 'ms')
    time_range = [40,100] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = '_mol_EPSP' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'Field induced in moleculare layer', sweeps = [4, 12, 8, 15, 18],
                               electrodes = [0,1,2, 3], y_range = [-5, 15], time_range = time_range) 
    
    if show_traces:
        plt.show()

def figure_exp_15_1(fig_type = '.png', show_traces = False):
    """ this cell was triggered to induce the EPSP (high CA + PTX) but it didn't"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 15.1)
    folder_save = save_folder + specific_folder + '_results/'    
    
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = '_noEPSP' + fig_type
    
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'No EPSP induced', sweeps = [1,3,5,7,9,10],
                               electrodes = [0,1,2, 3], y_range = [-10, 10], remove_avg = True,
                               time_range = [23, 48])  
    if show_traces:
        plt.show()   
    
    #folder_save,file_save,folder, file, x_scale = 'sec',
    #          title = 'Data', time_range = [], y_range =[-30, 70],
    #          electrodes = [],y_range_intra = []
    #display.plot_data(folder_save, file_save + fig_type,  folder_save,file_save, x_scale = 'ms',
    #                  y_range =[-10, 10])
    
    
    
    #import pdb; pdb.set_trace() 
 
def figure_exp_16(fig_type = '.png', show_traces = False):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 16)
    folder_save = save_folder + specific_folder + '_results/'
    time_range = [15, 45] # in ms
    y_range = [-15, 30]

    # plot every trace
    display.plot_data(folder_save,file_save + fig_type,folder_save,file_save,x_scale = 'ms', 
                      electrodes = [0,1,2],y_range =y_range, time_range =time_range)
    
    #display.plot_data(folder_save, file_save, x_scale = 'ms')

    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = '_EPSP_traces_pyr' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'Field induced in pyramidal layer', sweeps = [4, 18, 21, 25, 30],
                               electrodes = [0,1,2], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    
    if show_traces:
        plt.show()
    
def figure_exp_17(fig_type = '.png'):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 17)
    folder_save = save_folder + specific_folder + '_results/'
    
    #display.plot_data(folder_save, file_save, x_scale = 'ms')
    time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = '_synchrony' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'Field induced in moleculare layer', sweeps = [60],
                               electrodes = [0,1,2], y_range = [-550, 700], time_range = time_range) 
    
    
def figure_exp_18(fig_type = '.png', show_traces = False):    
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 18)
    folder_save = save_folder + specific_folder + '_results/'
    
    #display.plot_data(folder_save, file_save, x_scale = 'ms')
    time_range = [45, 75] # in ms
    y_range = [-15, 30]
    
    # plot every trace
    display.plot_data(folder_save,file_save + fig_type,folder_save,file_save,x_scale = 'ms', 
                      electrodes = [0,1,2],y_range =y_range, time_range =time_range)
    
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = '_EPSP_traces_mol' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'Field induced in moleculare layer', sweeps = [2, 3, 10, 20, 22, 35],
                               electrodes = [0,1,2], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_19(fig_type = '.png'):
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 19)
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'synchrony_' + fig_type
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', y_range = [])     
    
    #time_range = [35, 65] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    
    file_save = 'synch_events' + fig_type
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                               title = 'NBQX, 4AP, human subiculum, 10 events', 
                               sweeps = [0,2,3,4,5,7,8,9,10,11],
                               electrodes = [0,1,2,3],remove_avg = True, y_range = []) 
    plt.show()

def figure_exp_20(fig_type = '.png', save_traces = False, show_traces = False):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 20)
    file2save_npz = 'fig20_' + '.npz'
    
    file2save = 'interictal' + fig_type
    folder_save = save_folder + specific_folder + '_results/'
    y_range = [-15,90]
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 y_range=y_range, time_range = [51000,59000], electrodes=[1,2,3],
                 y_range_intra = y_range) 

    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = 25, el=3,
                     time_range=[-200,200], up = True, center_on_peak = True)
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [1,2,3],y_range =y_range)
        #import pdb; pdb.set_trace() 

    time_range = [100,300] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    file_save = 'interictal' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'interictal events', sweeps = [5,6,4,7,8,9,10,11,12,13],
                               electrodes = [1,2,3], y_range = [], time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()
     
def figure_exp_21(fig_type = '.png', save_traces = False, show_traces = False):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 21)
    file2save_npz = 'fig21_' + '.npz'
    
    file2save = 'PTX_block' + fig_type
    folder_save = save_folder + specific_folder + '_results/'
    y_range = [-15,90]
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 y_range=y_range, time_range = [68000,76000], electrodes=[1,2,3],
                 y_range_intra = y_range) 
    if show_traces:
        plt.show()


def figure_exp_22(fig_type = '.png',show_traces = True):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 22)
    
    folder_save = save_folder + specific_folder + '_results/'

    time_range = [0,350] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'exc_synch10' + fig_type
    #import pdb; pdb.set_trace()
    y_range = [-50,60]
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'exc synchrony10mM', sweeps = [5,6,4,7,8,9,10,11,12,13],
                               electrodes = [1,2,3], y_range = y_range, time_range = time_range,
                               remove_avg = True,y_range_intra = y_range) 
    if show_traces:
        plt.show()

def figure_exp_23(fig_type = '.png'):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 23)
    
    folder_save = save_folder + specific_folder + '_results/'

    time_range = [0,350] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'exc_synch12' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'exc synchrony12mM', sweeps = [5,6,10,11,12,13, 14, 15, 16, 17],
                               electrodes = [1,2,3], y_range = [], time_range = time_range,
                               remove_avg = True) 
    plt.show()

def figure_exp_24(fig_type = '.png'):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 24)
    file2save_npz = 'fig24_' + '.npz'
    
    file2save = 'NBQX_block' + fig_type
    folder_save = save_folder + specific_folder + '_results/'
    y_range = [-30,30]
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 y_range=y_range, time_range = [11000,19000], electrodes=[1,2,3],
                 y_range_intra = y_range) 


def figure_exp_25(fig_type = '.png', show_traces = False):
    """ interictal activity in the human slice"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 25)
    #file2save_npz = 'fig25_' + '.npz'
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'exc_synch_zoom' + fig_type
    y_range = [-500,700] #[-15,15]
    time_range =[3480,3510]    
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 y_range=[], time_range = time_range, electrodes=[0,1,2,3],
                 y_range_intra = [-50,0]) 
    
    file2save = 'exc_synch' + fig_type
    y_range = [-1000,1300] #[-15,15]
    time_range =[2800,3900]
    display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
                 y_range=y_range, time_range = time_range, electrodes=[0,1,2,3],
                 y_range_intra = []) 


    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'exc_synch_' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'sec',
                        title = 'excitatory synchrony', sweeps = [],
                               electrodes = [0,1,2,3], y_range = y_range, time_range = time_range,
                               remove_avg = True) 
    if show_traces:
        plt.show()

def figure_exp_26(fig_type = '.eps',save_traces = False, show_traces = False):
    """ GABAa synchrony cell1 (out of 2)"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 26)
    #file2save_npz = 'fig25_' + '.npz'
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'inh_synch_1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #             y_range=[], time_range = [], electrodes=[0,1,2,3],
    #             y_range_intra = []) 


    y_range = [-120,100]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'gaba_a_synch_1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'inhibitory synchrony', sweeps = [27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3], y_range = y_range, time_range = [],
                               remove_avg = True) 
    plt.show()

def figure_exp_27(fig_type = '.png', save_traces = False, show_traces = False):
    """ GABAa synchrony cell2 (out of 2)"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 27)
    file2save_npz = 'fig27_' + '.npz'
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'gaba_a_synch' + fig_type
    #y_range = [-500,700] #[-15,15]
    #time_range =[3480,3510]    
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'sec', 
    #             y_range=[], time_range = [], electrodes=[0,1,2,3],
    #             y_range_intra = [-50,0]) 
    #import pdb; pdb.set_trace()

    if save_traces:
        #it must be done only if the recording was gap free but 
        #it was not saved in the trace format yet

        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        dh.trigger_on_spike(folder_save, file_save, folder_save, file2save_npz, thresh = -25, el=3,
                     time_range=[-200,1000], up = False, center_on_peak = False)
        display.plot_data(folder_save,file2save,folder_save,file2save_npz,x_scale = 'ms', 
                          electrodes = [0,2,3],y_range =[])

    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file2save_npz, "data", "scale", "fs")
    file_save = 'gabaA_synch_fig27_group1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'GABAa synch, cell2', sweeps = [0,4,10,13],
                               electrodes = [0,2,3], y_range = [], time_range = [],
                               remove_avg = True) 
    file_save = 'gabaA_synch_fig27_group2' + fig_type    
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'GABAa synch, cell2', sweeps = [2,8,15,18,21],
                               electrodes = [0,2,3], y_range = [], time_range = [],
    
                               remove_avg = True) 

def figure_exp_28(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 28)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'high_calcium' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'high_calcium_cell1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [15,40],
                               remove_avg = True)   
    if show_traces:
        plt.show()
    

def figure_exp_29(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 29)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'inh_synch_1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [15,50],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_30(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 30)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'inh_synch_1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell2' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [15,50],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_31(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 31)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell3' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [15,50],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_32(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 32)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell4' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [15,50],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_33(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 33)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [30,70],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_34(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 34)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell2_1' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [45,70],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_35(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 35)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell2_2' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [45,70],
                               remove_avg = True)   
    if show_traces:
        plt.show()
        
def figure_exp_36(fig_type = '.eps',save_traces = False, show_traces = False):
    """ EPSP"""
    temp, save_folder, specific_folder, temp, file_save = get_figure_data_settings(fig_no = 36)
    
    
    folder_save = save_folder + specific_folder + '_results/'
    file2save = 'CA_ptx_cell1' + fig_type
 
    #display.plot_data(folder_save, file2save,folder_save,file_save,x_scale = 'ms', 
    #             y_range=[], time_range = [30,70], electrodes=[],
    #             y_range_intra = [],show_plot=True) 
    
    #import pdb; pdb.set_trace()
    y_range = [-20,20]
    #time_range = [] # in ms
    data_details = dh.read_npzdata(folder_save, file_save, "data", "scale", "fs")
    file_save = 'CA_ptx_cell2_3' + fig_type
    #import pdb; pdb.set_trace()
    display.plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'ms',
                        title = 'EPSP', sweeps = [],#[27,40,43,21,16], #2,8,16,21,23], #,27,40,43,48],
                               electrodes = [0,2,3,4,5,6,7,8,9,10,11], #e1 single, not in the tissue
                               y_range = y_range, time_range = [45,70],
                               remove_avg = True)   
    if show_traces:
        plt.show()
    
          
def save_all_as_npz(fig_no = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25]):
    #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19]
    """ saves all the data as .npz files for all the figures 
    specified in the fig_no; default are all the possible figures""" 
    

    
    for next_data in fig_no:
        # goes through every specified figure (data_folder and save_folder might
        # need to be altered
        data_folder, save_folder,specific_folder, data_file, file_save = get_figure_data_settings(fig_no = next_data)
    
        folder_data = data_folder + specific_folder + '/'
        folder_save = save_folder + specific_folder + '_results/'

        dh.save_data_as_npz(folder_data, data_file, folder_save, file_save,record_type='CA_ptx', traced=True, human=False, comments="")
        
    
    