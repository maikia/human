import data_handler as dh_temp
import display as display
import os
import data_handler as dh
import experimental_figs as exp

def playing_with_data():
    #folder_data = '/home/maja/PhDProject/human_data/data/'
    folder_data = '/home/maja/PhDProject/data/'
    folder_data='/home/maja/PhDProject/human_data/data/'
    folder_data ='/home/maja/PhDProject/data/'
    
    folder_specific = '2013_07_31/' #'HT_2013_04_02/'
    folder_specific = 'others/'
    folder_specific = '2013_08_10/'
    
    file_data = folder_specific + '2013_07_31_0002.abf' #2013_04_02_0013.abf'
    file_data = folder_specific + '2013_07_03 PR1_0000.abf'
    file_data = folder_specific + '2013_09_03_0002.abf'
    #file_data = folder_specific + '2013_09_03_0006.abf'
    file_data = folder_specific + '2013_09_05_0009_afterNBQX.abf'
    file_data = folder_specific + '2013_09_05_0019_synch.abf'
    file_data = folder_specific + '2013_09_05_0017.abf'
    file_data = folder_specific + '2013_10_08_0002.abf'
    
    folder_save = '/home/maja/PhDProject/data/2013_07_31/saved/'
    folder_save = '/home/maja/PhDProject/human_data/data/others/'
    
    file_save = folder_save + 'all_data_gabaB.npz'
    #file_save = folder_save + 'data.dat'
    
    data, scale, fs = dh_temp.read_data(folder_data, file_data)   
    dh_temp.save_data(folder_save, file_save, data, scale, fs)
    del data, scale, fs
    
    display.plot_data(folder_save, file_save, x_scale = 'ms')
    #display.plot_data_one_mean(folder_save, file_save, x_scale = 'ms',sweeps=[11,8,6,4]) #sweeps=[16,15, 13, 12, 11,10,9,8,7,6,4])
    #display.plot_data_one_mean(folder_save, file_save, x_scale = 'ms',sweeps=[1,40,55,62]) 
    #display.plot_data_one_mean(folder_save, file_save, x_scale = 'ms')

def plot_all_figures():
    """ draws and saves all the figures """
    fig_type = '.png'
    
    # params for fig 11 & fig 12
    
    
    # fig 11
    figure_exp_11(folder_save, file_fig11, fig_type = fig_type)
    
    # fig 12
    #file_fig12 = 
    'fig12_2013_10_08_0008_NBQX.npz'
    figure_exp_12(folder_save, file_fig12, fig_type = fig_type)
    
    
    folder_save = '/home/maja/PhDProject/data/2013_08_10_results/'
    file1 = '2013_10_08_0002_noNBAQ.npz'
    file2 = '2013_10_08_0008_NBQX.npz'    
    figure_exp_18(folder_save, file1, file2, fig_type = fig_type)

#exp.save_all_as_npz(fig_no = [25])
exp.figure_exp_11(fig_type = '.eps',show_traces = True) #,save_traces=False)

#exp.save_all_as_npz()

 
