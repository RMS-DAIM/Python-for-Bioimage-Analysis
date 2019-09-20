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

from matplotlib.widgets import Slider
from PIL import Image, ImageDraw
from skimage import io


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
    # Getting the number of frames
    n_frames = image.shape[2]

    # Converting the image Numpy array to PIL image and adding overlay elements
    image = render_overlay(image,tracks)
    
    # Creating the figure
    fig, (ax_image, ax_slider) = plt.subplots(2,1, gridspec_kw={'height_ratios':[20,1],'bottom':0.05,'top':0.95})
        
    # Method to run each time slider is changed
    def update_image(val):
        ax_image.clear()
        frame = int(round(val))
        ax_image.imshow(image[frame])
    
    # Creating the slider and running the image update for the first slice
    slider = Slider(ax_slider,'Slice',0, n_frames-1, valinit=0,valfmt="%0.0f")
    slider.on_changed(update_image)
    update_image(0)
    
    # Displaying the image
    plt.show()
    
## Converting the Numpy array to a PIL image and drawing tracks
def render_overlay(image, tracks):
    # Ensuring the tracks are sorted by frame
    tracks = tracks.sort_values(by=['T'])
    
    overlay_image = []
    for frame in range(0,image.shape[2]-1):
        print("Rendering frame ",frame)
        # Converting to PIL image
        overlay_image.append(Image.fromarray(image[:,:,frame]).convert('RGB'))
        
        # Adding overlay
        draw_tracks(overlay_image[frame],tracks,frame)
    
    return overlay_image

## Draw tracks for a single frame
def draw_tracks(image, tracks,frame):
    # Getting tracks to display (only show last 20 frames)
    tracks_to_show = tracks[:][(tracks['T'] > (frame-20)) & (tracks['T'] <=frame)]

    # Getting the unique tracks  
    track_IDs = tracks_to_show.TRACK_ID.unique()
    
    # Iterate over each track, drawing the path
    for track_ID in track_IDs:
        track = tracks_to_show[:][tracks_to_show['TRACK_ID'] == track_ID]
        draw = ImageDraw.Draw(image) 
        draw_track(draw, track)        

def draw_track(draw, track):
    for row in range(1,track.shape[0]-1):
        x1 = track.X.values[[row-1]]
        x2 = track.X.values[[row]]
        y1 = track.Y.values[[row-1]]
        y2 = track.Y.values[[row]]

        draw.line((x1,y1,x2,y2), fill=(255,0,255), width=5)

        
## Running these methods to check they work    
path = "..\\data\\ExampleTimeseries.tif"
image = load_images(path)

# Loading track coordinates
path = "..\\data\\TrackedCoordinatesNoHeader.csv"
coords = load_coordinates(path);

# Adding track renders
show_overlay(image,coords)
    