## 1.4.7_ImageAtrist
## DHampton RKolkemeir
## 10/24/16

import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def get_dem_pics(directory=None):
    """
    Insert desciption here
    """
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    
