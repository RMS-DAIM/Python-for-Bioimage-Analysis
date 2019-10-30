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
import sys

from colorsys import hsv_to_rgb
from ipywidgets import interact,IntSlider
from PIL import Image, ImageDraw
from skimage import io

## Image loading
def load_images(path):
    print("Loading images from \"",path,"\"")
    
    img = io.imread(path,plugin="pil")
    print("Loaded image shape: ",img.shape)
    
    img = np.transpose(img,(1,2,0))
    print("Reordered image shape: ",img.shape)
    
    # Adding a blank space to make the output easier to read
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
        names = ["ID","X","Y","FRAME","TRACK_ID"]
    elif raw.shape[1] == 6:
        names = ["ID","X","Y","FRAME","AREA","INTENSITY"]
    coords = pd.DataFrame(raw,columns=names)
    
    # We will need a blank column for TRACK_ID, so add it if necessary
    if coords.shape[1] == 6:
        coords['TRACK_ID'] = 0
    
    # Adding a blank space to make the output easier to read
    print(" ")
       
    return coords
    

## Create overlay
def show_overlay(image, tracks):
    # Getting the number of frames
    n_frames = image.shape[2]

    # Converting the image Numpy array to PIL image and adding overlay elements
    image = render_overlay(image,tracks)
    
    # Creating the figure
    plt.rcParams["figure.figsize"] = (8,6)
    plt.rcParams["toolbar"] = "None"
    fig, ax = plt.subplots()
    plt.tight_layout()
        
    # Method to run each time slider is changed
    def update_image(frame):
        frame = int(round(frame))
        ax.clear()
        ax.imshow(image[frame])

    # Creating the slider and running the image update for the first slice
    interact(update_image,frame=IntSlider(min=0, max=n_frames-1,step=1,value=0));
    
    # Displaying the image
    plt.show();
    
## Converting the Numpy array to a PIL image and drawing tracks
def render_overlay(image, tracks):
    # Ensuring the tracks are sorted by frame
    tracks = tracks.sort_values(by=['FRAME'])
    
    overlay_image = []
    n_frames = image.shape[2]
    for frame in range(0,n_frames):
        sys.stdout.write("\rRendering frame %d of %d" % ((frame+1),n_frames))
        # Converting to PIL image
        overlay_image.append(Image.fromarray(image[:,:,frame]).convert('RGB'))
        
        # Adding overlay
        draw_tracks(overlay_image[frame],tracks,frame)
        
    return overlay_image

## Draw tracks for a single frame
def draw_tracks(image, tracks,frame):
    # Getting tracks to display (only show last 20 frames)
    tracks_to_show = tracks[:][(tracks.FRAME > (frame-20)) & (tracks.FRAME <=frame)]

    # Getting the unique tracks  
    track_IDs = tracks_to_show.TRACK_ID.unique()
    
    # Iterate over each track, drawing the path
    for track_ID in track_IDs:
        track = tracks_to_show[:][tracks_to_show.TRACK_ID == track_ID]
        draw = ImageDraw.Draw(image) 
        draw_track(draw, track)        

def draw_track(draw, track):
    track_ID = track.TRACK_ID.iloc[0]
    
    for row in range(1,track.shape[0]-1):
        x1 = track.X.values[[row-1]]
        x2 = track.X.values[[row]]
        y1 = track.Y.values[[row-1]]
        y2 = track.Y.values[[row]]

        # Determining colour based on the track ID
        random.seed(track_ID)
        h = random.random()
        rgb = tuple(round(i*255) for i in hsv_to_rgb(h,1,1))
        draw.line((x1,y1,x2,y2), fill=rgb, width=3)
        