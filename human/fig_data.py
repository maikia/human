import data_handler as dh
import folder_handler as fh
import display as display
import pylab as plt
import numpy as np
import xlrd
import os.path
import folder_handler as fold


def get_dates_string(dates):
    year,month,day, number=dates
    # correct for missing 0s
    str_year=str(year)
    str_month=str(month)
    str_day = str(day)
    str_number=str(number)
    if len(str_month) < 2:
        str_month='0'+str_month
    if len(str_day) <2:
        str_day='0'+str_day     
    while len(str_number)<4:
        str_number = '0'+str_number  
    return str_year, str_month, str_day, str_number  
        
def get_data_folder(dates):
    data_folder = '/home/maja/PhDProject/data/'
    str_year,str_month,str_day, str_number = get_dates_string(dates)
    
    data_folder_temp = data_folder + str_year + '_' + str_month + '_' + str_day + '/'
    if not os.path.exists(data_folder_temp):
        data_folder = data_folder + 'HT'+str_year + '_' + str_month + '_' + str_day + '/'
    else: 
        data_folder = data_folder_temp
    #import pdb; pdb.set_trace() 
    return data_folder

def get_data_file(dates):
    str_year,str_month,str_day, str_number = get_dates_string(dates)
    data_file = str_year + '_' + str_month + '_' + str_day + '_' + str_number
    return data_file

def get_save_folder(dates, human=False):
    # return where the data is saved
    save_folder = '/home/maja/PhDProject/data/results/' 
    str_year,str_month,str_day, str_number = get_dates_string(dates)
    specific_folder = str_year + '_' + str_month + '_' + str_day

    # create new folder for storing figures for specific dates/numbers etc
    save_folder = save_folder + specific_folder + '/' + 'data_' + str_number + '/'
    fold.create_folder(save_folder)
    return save_folder
    
def get_file_save(dates):
    data_file = get_data_file(dates)
    file_save = 'data_' + data_file + '.npz'
    return file_save

def get_figure_data_settings(year, month, day, number, xls_file='/home/maja/PhDProject/data/data.xls',
                             force_save=False):
    """ here are saved all the parameters used for each figure 
    traced - is the data saved in traces (True) or in 'gap free' mode (False); (taken from the xls_file)
    checks if .npz file already exists, if not it will create .npz file
    unless force_save=True, than it overrides it no matter what"""
    dates = [year,month,day, number]
    data_folder = get_data_folder(dates)
    
    data_file = get_data_file(dates)
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    
    
    # shall we save it or not?
    if (not force_save) and (os.path.isfile(save_folder+file_save)):
        print 'found data file: '+save_folder+file_save
    else:
        print 'creating data file: '+save_folder+file_save
        # xls file where all the data is saved
        wb = xlrd.open_workbook(os.path.join(xls_file))
        
        wb.sheet_names()
        sheet_name = str(year)
        sh = wb.sheet_by_name(sheet_name)
        
        right_index = -1
        # find the row of interest
        for row_index in xrange(1,sh.nrows): 
            # check if the same month
            #import pdb; pdb.set_trace() 
            true_month = int(sh.col(2)[row_index].value)==month
            true_day = int(sh.col(3)[row_index].value)==day
            true_number = int(sh.col(4)[row_index].value)==number
            
            if true_month and true_day and true_number:
                right_index = row_index
                break
              
        if right_index == -1:
            raise Exception("This data does not exist: "+str(year) + ' '+str(month)+ ' '+str(day)+' '+str(number))
        record_type = sh.cell(right_index, 5).value
        traced = sh.cell(right_index, 6).value
        human = sh.cell(right_index, 7).value
        comments = sh.cell(right_index, 8).value
        
        if human:
            human = True
        else:
            human = False
        
        #import pdb; pdb.set_trace()   
        if traced:
            traced = True
        else:
            traced = False
        
        data_file = data_file + '.abf'
        
        # save the parameters to .npz file
        dh.save_data_as_npz(data_folder, data_file, save_folder, file_save,
                            record_type, traced, human, comments)
        print 'all saved in: ' + save_folder+file_save

def make_all_figures(dates, use_available_json=False):
    """ it proceeds given params as:
    data_folder, save_folder, data_file + '.abf', file_save, record_type, traced, human, comments
    and uses json file if available and if use_available_json is set to True
    It will save all the figures in the files in the given folder """
    
    
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    
    # acquire params for saving full data
    msg = 'Do you want to update full data params? '
    var = acquire_user_input(msg,possibility=['y','n'])
    
    if var == 'y':
        full_data_params = acquire_full_data_params(save_folder, file_save)
    
    # check if data needs to be triggered
    [traced]=dh.read_npzdata(save_folder, file_save, "traced")
    
    var = 'y'
    msg = 'Do you want to filter the data? '
    while var == 'y':
        var = acquire_user_input(msg,possibility=['y','n'])
        msg = 'Do you want to filter the data differently? [Only last filtering will be saved for future figure]'
        
        filtered_params = acquire_filtered_params(save_folder, file_save)
    
    import pdb; pdb.set_trace() 
        
    #dh.trigger_on_spike(folder_save, new_file, folder_save, file2save_filtnpz, thresh = -30, el=0,
    #             time_range=[-15,50])
    
    
    if not traced: 
        full_data_params = acquire_traced_data
        
    print ' you entered: ', var
    divide_data_to_traces(dates)

def filter_data(dates):
    """ check if the data should be filter and filter it if necessary;
        save all the filtered data along with non-filtered data"""
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    
    var = 'y'
    msg = 'Do you want to filter the data differently?'
    all_filtered_params = []
    while var == 'y':
        filtered_params = acquire_filtered_params(save_folder, file_save)    
        var = acquire_user_input(msg,possibility=['y','n'])
        all_filtered_params.append(filtered_params)
    return all_filtered_params
        

def process_data(dates, use_available_json, xls_file):
    """ runs all the necessary functions to gather the data and make the figures for the given data
    eg: dates=[2013, 4,2,13]
    """
    get_figure_data_settings(dates[0], dates[1], dates[2], dates[3], xls_file)
    
    msg = 'Do you want to update full data params? '
    var = acquire_user_input(msg,possibility=['y','n'])
    if var == 'y':
        full_data_params = acquire_full_data_params(dates)# for full data display
    
    msg = 'Do you want to update filtered data params? '
    var = acquire_user_input(msg,possibility=['y','n'])
    if var == 'y':
        filtered_params = filter_data(dates)
    
    # check if data needs to be triggered
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    [traced]=dh.read_npzdata(save_folder, file_save, "traced")
    if traced == False:
        msg = 'Original data is not divided to traces, do you want to divide it now? '
        var = acquire_user_input(msg,possibility=['y','n'])
        if var == 'y':
            traced_params = divide_data_to_traces()
    else:
        print "The original data is divided to traces, would you like to choose params for the displayed figure? "
        var = acquire_user_input(msg,possibility=['y','n'])
        if var == 'y':
            pass
            # ---> here acquire params for the traced figure
            # traced_params[,full_data_params[-1]]
        #traced_params = full_data_params
    
    make_all_figures(dates)
    #make_all_figures(received_params,use_available_json)
    prepare_json_file(dates)

    
    
def run_data(dates=[],use_available_json=False):
    """ runs all the data, all the figures if no params are given,
    eg: dates=[2013,4,2,13]
    otherwise you must pass the [year, month,day and number] of the file you want to proceed
    and the function will make all the possible figures for this params 
    
    if the data was already evaluated, and use_available_json is set to True, it will use it,
    otherwise it will use only the defaults"""
    
    xls_file = '/home/maja/PhDProject/data/data.xls'
    if len(dates) == 0:
        # process all the figs
        all_data = get_available_data(xls_file)
        for next_data_file in range(len(all_data)):
            process_data(dates[next_data_file], use_available_json, xls_file)
    else:
        process_data(dates, use_available_json, xls_file)       


def divide_data_to_traces(dates):
    """ it must be done only if the recording was gap free but 
    it was not saved in the trace format yet"""
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    var = 'y'
    msg = 'Do you want to divide different data or the same data differently?'
    all_traced_params = []
    while var == 'y':
        traced_params = acquire_traced_params(save_folder, file_save)    
        var = acquire_user_input(msg,possibility=['y','n'])
        all_traced_params.append(traced_params)
        # ---> check should be done if the same file was not saved twice and if yes, the previous 
    return all_traced_params
        
        
    msg = 'Which data do you want to divide to traces? '
    
    dh.trigger_on_spike(folder_save, new_file, folder_save, file2save_filtnpz, thresh = -30, el=0,
                     time_range=[-15,50])
    
    
    if True:
        #display.plot_data(folder_save,file2save,folder_save,file_save,x_scale = 'ms')#,time_range=time_range)
        new_file = 'filtered_data_above500.npz'
        #dh.filter_data(folder_save, file_save, folder_save, new_file, 500.0, 
        #        electrodes = [2],N = 100, filter_type = 'high_pass')
        
        #
        
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

def get_available_data(xls_file='/home/maja/PhDProject/data/data.xls', print_out=False):
    """ reads from the given xls file available datas to proceed; If print_out == True,
    it will print it out"""
    wb = xlrd.open_workbook(os.path.join(xls_file))
    all_data = []
    for next_sheet in range(wb.nsheets):
        sh = wb.sheet_by_index(next_sheet)
        for next_row in range(1,len(sh.col(0))):
            year = int(sh.col(1)[next_row].value)
            month = int(sh.col(2)[next_row].value)
            day = int(sh.col(3)[next_row].value)
            number = int(sh.col(4)[next_row].value)
            all_data.append([year,month,day,number])
            if print_out:
                record_type=sh.col(5)[next_row].value
                traced=sh.col(6)[next_row].value
                human=sh.col(7)[next_row].value
                to_print= "year: "+str(year)+", month: "+str(month)+", day: "+str(day)+", file no:"+str(number)
                to_print=to_print+ ', ' + record_type
                if traced: 
                    to_print = to_print + ', traced'
                if human:
                    to_print = to_print + ', human'
                print to_print
    all_data = np.array(all_data)
    
    return all_data

def acquire_user_input(msg,possibility=[]):
    var = ''
    print_pos=''
    for g in range(len(possibility)):
        print_pos=print_pos+str(possibility[g])+'/'

    if len(possibility)>0:
        while not (var in possibility):
            var = raw_input(msg+"[" + print_pos+"]: ")
    else:
        var = raw_input(msg)
    return var
            

def convert_to_list(input_string):
    """ converts two string list to two double list, or empty list if strings are empty)"""
    if len(input_string[0]) == 0 or len(input_string[1]) ==0:
        return []
    else:
        return [float(input_string[0]),float(input_string[1])]

def acquire_basic_fig_params():
    """ asks the user for the parameters which should be used when displaying the figure"""
    msg='How will you want the data to be displayed in saved figure'
    time_type = acquire_user_input(msg,['ms','sec','min'])
    
    msg='Title for the future full data figure: '
    fig_title = acquire_user_input(msg)
    
    msg='Electrodes which you want to use (starting from 0)[eg 0,1,2]:'
    electrodes = acquire_user_input(msg)
    if len(electrodes) > 0:
        if electrodes[-1] == ',':
            electrodes = electrodes[:-1]
        electrodes = map(int, electrodes.split(',')) # map string to list of integers
    else:
        electrodes = []
    
    msg='min for y scale of intra (type enter if you want to use default):'
    y_scale_min_intra = acquire_user_input(msg)
    msg='max for y scale of intra type enter if you want to use default):'
    y_scale_max_intra = acquire_user_input(msg)
    y_scale_intra = convert_to_list([y_scale_min_intra,y_scale_max_intra])
    
    msg='min of time range (type enter if full data range):'
    time_range_min = acquire_user_input(msg)
    msg='max of time range (type enter if full data range):'
    time_range_max = acquire_user_input(msg)
    time_range = convert_to_list([time_range_min,time_range_max])
    
    msg='min for y scale of extracellular:'
    y_scale_min_extra = acquire_user_input(msg)
    msg='max for y scale of extracellular:'
    y_scale_max_extra = acquire_user_input(msg)        
    y_scale_extra = convert_to_list([y_scale_min_extra,y_scale_max_extra])
    return y_scale_intra,time_range,y_scale_extra,time_type,fig_title,electrodes

def acquire_full_data_params(dates):
    """ ask the user to give all the parameters needed to display full data """
    
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    full_data_npz_file = file_save
    msg='Do you want to display full data now?'
    var = acquire_user_input(msg,['y','n'])
    again = True
    plt.ion()
    if var == 'y':
        # display full data if requested            
        fig_full = display.plot_data(save_folder,'temp',save_folder,file_save,x_scale='ms',
                          title = 'Whole data',time_range=[],y_range=[],
                          electrodes=[],y_range_intra=[],show_plot=True,
                          save_plot=False)
        plt.draw()

    while again:
        
        fig_params = acquire_basic_fig_params()
        full_data_y_scale_intra,full_data_time_range,full_data_y_scale_extra,full_data_time_type,full_data_title,full_data_electrodes = fig_params
        
        plt.ion()
        fig = display.plot_data(save_folder,'full_data',save_folder,file_save,x_scale=full_data_time_type,
                title = full_data_title,time_range=full_data_time_range,y_range=full_data_y_scale_extra,
                electrodes=full_data_electrodes,y_range_intra=full_data_y_scale_intra,show_plot=True,
                save_plot=True)     
        plt.draw()  
        msg='Are you happy with the results?:'
        enough = acquire_user_input(msg,['y','n'])
        plt.close(fig)
        
        if enough == 'y':
            again = False
        
    return [fig_params, full_data_npz_file]

def acquire_filtered_params(save_folder,file_save):
    #dh.read_npzdata(save_folder, file_save, "data", "scale", "fs")
    
    msg='Electrodes which you want to use (starting from 0)[eg 0,1,2]:'

    filtered_electrodes = acquire_user_input(msg)
    if len(filtered_electrodes) > 0:
        if filtered_electrodes[-1] == ',':
            filtered_electrodes = filtered_electrodes[:-1]
        filtered_electrodes = map(int, filtered_electrodes.split(',')) # map string to list of integers
    else:
        filtered_electrodes = []
    
    msg = 'Which kind of filter do you want to use'
    filter_type = acquire_user_input(msg,['hp','lp','bp'])
    if filter_type == 'hp':
        filter_type = 'high_pass'
        msg = 'What is the frequency border?'
        filter_freq = acquire_user_input(msg)
        filter_freq = float(filter_freq)
    elif filter_type == 'lp':
        filter_type = 'low_pass'
        msg = 'What is the frequency border?'
        filter_freq = acquire_user_input(msg)
        filter_freq = float(filter_freq)
    elif filter_type == 'bp':
        filter_type = 'band_pass'
        msg = 'What is the frequency border from below?'
        filt_freq1 = acquire_user_input(msg)
        msg = 'What is the frequency border from above?'
        filt_freq2 = acquire_user_input(msg)
        filter_freq=[float(filt_freq1,filt_freq2)]
    
    filter_data_file = 'filtered_' + filter_type + str(filter_freq) + '.npz'
    plt.close()
    
    dh.filter_data(save_folder, file_save, save_folder, filter_data_file, filter_freq, 
            electrodes = filtered_electrodes, N = 100, filter_type = filter_type)

    print 'data saved under: ' + save_folder + filter_data_file
    msg='Would you like to view the results?: '
    view_results = acquire_user_input(msg,['y','n'])
    if view_results == 'y':
        plt.ion()
        fig_filt = display.plot_data(save_folder,'temp',save_folder,filter_data_file,x_scale='ms',
                  title = 'Filtered data',time_range=[],y_range=[],
                  electrodes=[],y_range_intra=[],show_plot=True,
                  save_plot=False)
        plt.draw()

        fig_params = acquire_basic_fig_params()
        fig_params
        
        plt.close(fig_filt) # close the figure
        
    return [filter_type, filtered_electrodes, filter_freq, fig_params, filter_data_file]


def prepare_json_file(dates, fig_type='.png', time_type='ms',save_plots=False):
    """ eg: dates=[2013, 4,2,13] 
    it will display all the data the way, so that the params for .json file can be easily chosen """
    
    save_file = 'whole_data' + fig_type
    plt.ion()
    save_folder = get_save_folder(dates)
    file_save = get_file_save(dates)
    
    # data to be used in .json files
    # fig_params = y_scale_intra,time_range,y_scale_extra,time_type,fig_title,electrodes
    # full data params
    # [fig_params, full_data_npz_file]
    
    # filtered data params (might be multiple if more than one filter was used
    # [filter_type, filtered_electrodes, filter_freq, fig_params, filter_data_file]
    
    

    
    

#get_available_data('/home/maja/PhDProject/data/data.xls') 
#get_available_data(print_out=True)
run_data(dates=[2013,4,2,13])
"""
    fig_no, fig_type='.png',save_traces=False,show_traces=False,
                 time_type='ms',time_range=[],y_range=[],
                 plot_all_data=False,save_all_data_plot=False,
                 thres=1.0, el=0, up=True, center_on_peak=False,

     common parameters, override if different
    data_folder, save_folder = common_data()
    data_folder = data_folder
    save_folder = save_folder + specific_folder
    
    file_save = 'fig' + str(fig_no) + '_' + data_file + record_type + '.npz' 
    data_file + '.abf'
"""


"""
What to allow the user:
1. check from the xls file the details, display info about the data
input:   folder_name, file_name
output:  text info about the data, 
2. filter the data
input:    folder_name, file_name to filter (it could be row data or already traced etc), save_place
            all info about how to filter it (hp, frequency, etc)
output:   filtered data, text info about where it was saved
3. Divide the data to traces
input:    folder_name, file_name to trace (it could be filtered or row data, etc), save_place
            all the details about how to divide to traces (thresh, electrode, etc)
output:   traced data, text info about where it was saved


"""