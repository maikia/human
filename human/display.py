import numpy as np
import data_handler as dh
import pylab as plt
import matplotlib.ticker as tic
#import scroll as scroll


def plot_data_one_mean(data_details, folder_save, file_save, x_scale = 'sec', title = 'Data', sweeps = [], electrodes=[],time_range=[],
                       y_range = [-30, 70], y_title = 'Voltage (mV)',
                       y_range_intra = [], remove_avg = False):
    """ reads and then plots given data in one plot, and calculates average,
    sweeps can be selected; if sweeps = [], all will be plotted
    x_scale - time scale in which to display the data, possible options:
    'ms', 'sec', 'min' """   
    [data, y_scale, fs] = data_details #dh.read_npzdata(folder, file, "data", "scale", "fs")
   
    #import pdb; pdb.set_trace() 
    #data = data[:,:,::3000]
    if sweeps == []:
        data = data[:,:,:]
    else:
        data = data[:,:,:]
        data = data[:,sweeps,:]
        
    if electrodes!=[]:
        data=data[electrodes,:,:]     
           
    if time_range != []:
        time_pts1 = dh.ms2pts(time_range[0], fs)
        time_pts2 = dh.ms2pts(time_range[1], fs)
        data=data[:,:,time_pts1:time_pts2] 
        
    plot_color = '0.5'
    fig = plt.figure()
   
    for trace in range(np.size(data, 1)):

        if not remove_avg:
            plot_one_data(data[:,trace,:], title, fs, x_scale, y_scale, plot_color,
                          y_range=y_range, y_title=y_title)
        elif remove_avg:
             
            calc_avg = np.average(data[:,trace,0:100],1)
            data[:,trace,:]=data[:,trace,:]-np.transpose(np.resize(calc_avg,(len(data[0,0,:]),len(calc_avg))))
            plot_one_data(data[:,trace,:], title, fs, x_scale, y_scale, plot_color,
                          y_range=y_range, y_title=y_title)
    avg = np.mean(data[:,:,:],1)
    
    plot_one_data(avg, title, fs, x_scale, y_scale, 'k', lw=3,
                          y_range_intra = y_range_intra, y_range=y_range, y_title=y_title)    
    #plt.title(title)
    #print title
    #print folder_save+file_save
    plt.savefig(folder_save+file_save)


def plot_one_data(data_trace, tit, fs, x_scale, y_scale, plot_color, lw=2,
                  y_range_intra = [],y_range = [-30, 70], y_title = 'Voltage (mV)'):
    
    t = dh.get_timeline(data_trace[0, :], fs, scale = x_scale)
    
    # define title for the figure

    ax = None
    #import pdb; pdb.set_trace()
    use_electrodes = range(len(data_trace)) # [0,1] 
    for electr in use_electrodes:
        
        ax = plt.subplot(len(use_electrodes), 1, electr + 1, sharex=ax)#len(data_trace), 1, electr + 1, sharex=ax)
        
        data_electr = data_trace[electr, :]
        
        plt.plot(t, data_electr, plot_color, lw=lw)
        
        if electr == 0:
            plt.title(tit)
            if y_range_intra != []:
                plt.ylim(y_range_intra)
        else:    
            ax.title.set_visible(False)
            if y_range != []:
                plt.ylim(y_range)
            #plt.ylim([-400,1200])
            
        
        if electr != len(data_trace) -1:
            plt.subplots_adjust(hspace = .001)
            #ax.set_xticklabels(())
        temp = tic.MaxNLocator(3)
        ax.yaxis.set_major_locator(temp)        
        plt.xlim([0, max(t)])
        plt.ylabel(y_title)
        
    plt.xlabel('Time ('+x_scale + ')')
    

def plot_data(folder_save,file_save,folder, file, x_scale = 'sec',
              title = 'Data', time_range = [], y_range =[-30, 70],
              electrodes = [],y_range_intra = []):
    """ reads and then plots given data
    x_scale - time scale in which to display the data, possible options:
    'ms', 'sec', 'min'; time_range is given in 'ms' """
    # import pdb; pdb.set_trace() 
    
    # read the data
    [data, y_scale, fs] = dh.read_npzdata(folder, file, "data", "scale", "fs")

    if electrodes!=[]:
        data=data[electrodes,:,:]   
        
    if time_range != []:
        time_pts1 = dh.ms2pts(time_range[0], fs)
        time_pts2 = dh.ms2pts(time_range[1], fs)
        data = data[:,:,time_pts1:time_pts2]
        
        
    plot_color = 'k'
    for trace in range(np.size(data, 1)):
        fig = plt.figure()
        if np.size(data,1) > 1:
            tit = title + ', trace ' + str(trace)
        else:
            tit = title
        plot_one_data(data[:,trace,:], tit, fs, x_scale, y_scale, plot_color, y_range=y_range, 
                      y_range_intra = y_range_intra)
        plt.savefig(folder_save+str(trace) +file_save)
        plt.show()
    

    
    
    
    
        
        
        