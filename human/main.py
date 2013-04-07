import data_handler as dh_temp
import display as display
import os

folder_data = '/home/maja/phdProject/human_data/data/'
file_data = '2013_04_02_0013.abf'
folder_save = '/home/maja/phdProject/human_data/saved/'
file_save = 'all_data.npz'


data, scale, fs = dh_temp.read_data(folder_data, file_data)   
dh_temp.save_data(folder_save, file_save, data, scale, fs)
del data, scale, fs
display.plot_data(folder_save, file_save)



