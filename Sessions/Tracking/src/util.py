## UTILITIES FOR TRACKING COURSE
# (Add information here)

## Importing dependencies
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import sys

from colorsys import hsv_to_rgb
from ipywidgets import interact,IntSlider
from os import listdir
from PIL import Image, ImageDraw
from skimage import io

downsample = 4

def load_images(path):
    print("Loading images from \"",path,"\"")
    
    file_list = listdir(path)
    
    # Getting first image as an example
    temp_im = io.imread(path+file_list[0],plugin="pil")
    temp_im = temp_im[0:temp_im.shape[0]:downsample,0:temp_im.shape[1]:downsample]
    im = np.zeros((temp_im.shape[0],temp_im.shape[1],len(file_list)))
    
    print("")
    for i,file in enumerate(listdir(path)):       
        sys.stdout.write("\rReading image %i of %i" % ((i+1),len(file_list)))
        temp_im = io.imread(path+file,plugin="pil")
        temp_im = temp_im[0:temp_im.shape[0]:downsample,0:temp_im.shape[1]:downsample]
        im[:,:,i] = temp_im
        
    print("")
    print("Loaded image shape: ",im.shape)
        
    return im
   

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
    raw = np.genfromtxt(path,delimiter=",",skip_header=1)
    print("Loaded data shape: ",raw.shape)

    # Adding data to Pandas DataFrame, so we can have headers
    # Add a final column for Track ID present
    names = ["ID","X","Y","FRAME","AREA","TRACK_ID"]
    coords = pd.DataFrame(raw,columns=names)
    
    # We're using downsampled data for speed of processing.  Applying this to X and Y.
    coords.X = coords.X/downsample
    coords.Y = coords.Y/downsample
        
    # Adding a blank space to make the output easier to read
    print(" ")
       
    return coords
    

## Create overlay
def show_overlay(image, coords, show_tracks):
    # Getting the number of frames
    n_frames = image.shape[2]

    # Converting the image Numpy array to PIL image and adding overlay elements
    image = render_overlay(image,coords,show_tracks)
    
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
def render_overlay(image, coords, show_tracks):
    # Ensuring the tracks are sorted by frame
    coords = coords.sort_values(by=['FRAME'])
    
    overlay_image = []
    n_frames = image.shape[2]
    for frame in range(0,n_frames):
        sys.stdout.write("\rRendering frame %d of %d" % ((frame+1),n_frames))
        # Converting to PIL image
        overlay_image.append(Image.fromarray(image[:,:,frame]).convert('RGB'))
        
        # Adding points overlay
        draw_points(overlay_image[frame],coords,frame)
        
        # Adding tracks overlay
        if show_tracks:
            draw_tracks(overlay_image[frame],coords,frame)
        
    return overlay_image

## Draw points for a single frame
def draw_points(image,coords,frame):
    # Getting tracks to display (only show last 20 frames)
    rows = coords.index[coords.FRAME == frame]
                        
    # Iterate over each point, drawing it on the image
    for row in rows:
        draw = ImageDraw.Draw(image) 
        draw_point(draw, coords.loc[row])
                    
def draw_point(draw,point):
    # Setting the radius of the points
    r = 2
    
    x = point.X
    y = point.Y
    
    draw.ellipse(((x-r,y-r),(x+r,y+r)),fill=(255,0,0))
                    
## Draw tracks for a single frame
def draw_tracks(image,coords,frame):
    # Getting tracks to display (only show last 20 frames)
#     tracks_to_show = coords[:][(coords.FRAME > (frame-20)) & (coords.FRAME <=frame)]
    tracks_to_show = coords[:][(coords.FRAME <=frame)]

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
        draw.line((x1,y1,x2,y2), fill=rgb)
        