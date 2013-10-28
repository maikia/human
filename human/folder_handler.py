import data_handler as dh_temp
import display as display
import os

def create_folder(folder):
    """ checks if given folder exists and creates it if it does not"""
    if not os.path.exists(folder):
        os.makedirs(folder)
        
def file_exists(full_path):
    """ checks if given file exists in the given folder (full path must
    be given"""
    try:
        with open(full_path): pass
    except IOError:
        raise Exception(full_path + " does not exist")
    
def check_type(file):
    """ checks and returns the type of the given file"""
    return file.split(".")[-1]



    