import numpy as np
import data_handler as dh
import pylab as plt
import matplotlib.ticker as tic
import scroll as scroll

def plot_data(folder, file, x_scale = 'sec', title = 'Data'):
    """ reads and then plots given data
    x_scale - time scale in which to display the data, possible options:
    'ms', 'sec', 'min' """
    # import pdb; pdb.set_trace() 
    
    # read the data
    [data, y_scale, fs] = dh.read_npzdata(folder, file, "data", "scale", "fs")
        
    for trace in range(np.size(data, 1)):
        fig = plt.figure()
        data_trace = data[:, trace, :]
        
        t = dh.get_timeline(data_trace[0, :], fs, scale = x_scale)
        
        # define title for the figure
        if np.size(data,1) > 1:
            tit = title + ', trace ' + str(trace)
        else:
            tit = title
        
        for electr in range(len(data_trace)):
            
            ax = plt.subplot(len(data_trace), 1, electr + 1)
            
            data_electr = data_trace[electr, :]
            
            plt.plot(t, data_electr)
            
            if electr == 0:
                plt.title(tit)
            else:    
                ax.title.set_visible(False)
            
            if electr != len(data_trace) -1:
                plt.subplots_adjust(hspace = .001)

                ax.set_xticklabels(())
            temp = tic.MaxNLocator(3)
            ax.yaxis.set_major_locator(temp)        
            plt.xlim([0, max(t)])
            plt.ylabel('Voltage (' + str(y_scale[electr]) + "), " +str(electr))
            
        plt.xlabel('Time (' + x_scale + ")")
        
    plt.show()
    return fig
        
        