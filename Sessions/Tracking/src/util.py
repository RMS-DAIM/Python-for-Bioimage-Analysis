## UTILITIES FOR TRACKING COURSE
# (Add information here)


## Installing dependencies
# (Is this necessary?)


## Importing dependencies
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import matplotlib.lines as lines

from skimage import io
from matplotlib.widgets import Slider


## Image loading
def load_images(path):
    print("Loading images from \"",path,"\"")
    
    img = io.imread(path,plugin="pil")
    print("Loaded image shape: ",img.shape)
    
    img = np.transpose(img,(1,2,0))
    print("Reordered image shape: ",img.shape)
    
    print(" ")
    
    # Return the loaded array
    return img


## Coordinate loading
# Loading coordinates from a CSV file. Each row of the output corresponds to a single timepoint 
# instance of an object and contains the instance ID ("ID"), x-centroid ("X"), y-centroid ("Y"), 
# timepoint ("T"), object area ("AREA") and object intensity ("INTENSITY").

# Data is stored in a Pandas DataFrame, so the individual columns can be accessed by their name. 
# For example, if we call our DataFrame "data", then we can get the entire X column using:
#     value = data["X"]

# Similarly, to get just the 4th element of the X column we use:
#     value = data["X"][3]

def load_coordinates(path):
    print("Loading coordinates from \"",path,"\"")
    
    # Loading raw data into Numpy array
    raw = np.genfromtxt(path,delimiter=",")
    print("Loaded data shape: ",raw.shape)

    # Adding data to Pandas DataFrame, so we can have headers
    # Add a final column for Track ID present
    if raw.shape[1] == 5:
        names = ["ID","X","Y","T","TRACK_ID"]
    elif raw.shape[1] == 6:
        names = ["ID","X","Y","T","AREA","INTENSITY"]
    data = pd.DataFrame(raw,columns=names)
    
    print(" ")
       
    return data
    

## Create overlay
def show_overlay(image, tracks):
    # Creating the figure
    fig, (ax_image, ax_slider) = plt.subplots(2,1, gridspec_kw={'height_ratios':[20,1],'bottom':0.05,'top':0.95})
        
    # Method to run each time slider is changed
    def update_image(val):
        ax_image.clear()
        slice = int(round(val))
        ax_image.imshow(image[:,:,slice])
        draw_tracks(ax_image,tracks,frame)
    
    # Creating the slider and running the image update for the first slice
    slider = Slider(ax_slider,'Slice',0, image.shape[2]-1, valinit=0,valfmt="%0.0f")
    slider.on_changed(update_image)
    update_image(0)
    
    # Displaying the image
    plt.show()
    
    
## Draw tracks for a single frame
def draw_tracks(ax, tracks,frame):
    # Getting the row index of each coordinate in the previous frame
    
    # Iterating over each track in the current frame, adding it to the overlay
    x1 = random.randint(0,100)
    x2 = random.randint(0,100)
    y1 = random.randint(0,100)
    y2 = random.randint(0,100)
    line = lines.Line2D([x1,x2],[y1,y2])
    line.set_linewidth(1)
    line.set_color('r')
    ax.add_line(line)    


## Running these methods to check they work    
path = "..\\data\\ExampleTimeseries.tif"
image = load_images(path)

# Loading track coordinates
path = "..\\data\\TrackedCoordinatesNoHeader.csv"
coords = load_coordinates(path);

# Adding track renders
show_overlay(image,coords)
    