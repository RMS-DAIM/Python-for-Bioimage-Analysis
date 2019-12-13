import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import cv2 as cv
import glob # interacting with filesystem
import skimage.io #reading png files
from skimage.transform import resize


# Hypothesis is a combination of variables X
# Y = x_a * (sin(x_b)) + x_c^2
def generateNiceData(noVariable, train_samples, noNoise=False):
    scale_a, scale_b, scale_c = 10, 5, 1
    x_a = scale_a * np.random.random_sample((train_samples,1))
    x_b = scale_b * np.random.random_sample((train_samples,1))
    x_c = scale_c * np.random.random_sample((train_samples,1))
    x_d = np.random.random_integers(0,5,train_samples)

    Y_a = x_a + np.random.normal(0,1, train_samples).reshape(-1, 1)
    Y_b = 10 * np.sin(x_b) + np.random.normal(0,1, train_samples).reshape(-1, 1)
    Y_c = 10* np.power(x_c,4)  + np.random.normal(0,1, train_samples).reshape(-1, 1)
    Y_d = (1-2*(x_d%2)).reshape(-1, 1)

    if noNoise:
        Y_a = x_a 
        Y_b = 10 * np.sin(x_b)
        Y_c = 10* np.power(x_c,4) 
        Y_d = (1-2*(x_d%2)).reshape(-1, 1)


    if noVariable == 1:
        Y = Y_a - 5
    if noVariable == 2:
        Y = Y_b - 0.1 * Y_a
    if noVariable == 3:
        Y = Y_a + Y_b - Y_c
    if noVariable == 4:
        Y = (Y_a + Y_b - Y_c) * Y_d

    Y_class = np.sign(Y)
    #plt.plot(x_a,Y_a,'o')
    #plt.plot(x_b,Y_b,'o')
    #plt.plot(x_c,Y_c,'o')
    #plt.plot(x_d,Y_d,'o')
    #plt.show()
    #plt.plot(Y)
    #plt.plot(Y_class)
    #plt.show()

    dataset = pd.DataFrame({'A': x_a.flatten(),
                            'B': x_b.flatten(),
                            'C': x_c.flatten(),
                            'D': x_d.flatten(),
                            'Y': Y.flatten(),
                            'Y_class': Y_class.flatten()
                            })
    if noVariable < 4:
        del dataset['D']
    if noVariable < 3:
        del dataset['C']
    if noVariable < 2:
        del dataset['B']
    return dataset



def showBlobs(blobdf):
    howmany = blobdf.shape[0]
    howmany = 4 * (howmany//4)
    fig, ax = plt.subplots(howmany//4, 4, figsize=(3 * (1 + howmany//4), 3 * (1 + howmany//4)))
    axes = ax.flatten()
    plot_idx = 0
    for index, row in blobdf.iterrows():
        if (plot_idx==4 * (howmany//4)):
            break
        axes[plot_idx].imshow(row['raw_data'])
        axes[plot_idx].set_title('Known Class: {0}'.format(row['class']))
        axes[plot_idx].get_yaxis().set_visible(False)
        axes[plot_idx].get_xaxis().set_visible(False)
        plot_idx = plot_idx + 1
#     fig.tight_layout()
    plt.show()


def generateBlobsData(imageDir, noClasses, trainSamples, imSize=64, noiseSize=25, colour=False):

    all_blob_files = glob.glob(imageDir + "*png")

    #blob_class as name/int
    intblobclass={'bloby':0,'wavey':1,'spikey':2, 'misty':3, 'ellipsy':4, 'ringey':5}
    intblobclass.update({'ringey-wavey-1':6,'ringey-wavey-2':7,'ringey-wavey-3':8,'ringey-wavey-4':9,'ringey-wavey-5':10,'ringey-wavey-6':11})
    blob_data= pd.DataFrame(columns=['class', 'raw_data'])

    for blob_file in all_blob_files:
        blob_class = blob_file.split("/")[-1].split("_")[0]
        blob_class_int=intblobclass[blob_class]
        if(noClasses <= blob_class_int):
            continue
        #TASK - what will happen if we use resize function from skimage library?
        #blob_image = skimage.io.imread(blob_file,as_gray=True)
        #blob_image_resized = resize(blob_image, (64,64), anti_aliasing=False)
        blob_image = cv.imread(blob_file)
        #add noise
        if noiseSize>0:
            row,col,ch= blob_image.shape
            gauss = np.random.normal(0,noiseSize,(row,col,ch))
            gauss = gauss.reshape(row,col,ch)
            blob_image = np.abs(blob_image - gauss)
            blob_image = blob_image.astype(np.uint8)
        if not colour:
            blob_image = cv.cvtColor(blob_image, cv.COLOR_BGR2GRAY)
        blob_image_resized = cv.resize(blob_image, (imSize,imSize), interpolation = cv.INTER_AREA)
        blob_feats = {'class':blob_class_int,
                    'raw_data':blob_image_resized
                    }
        blob_data = blob_data.append(blob_feats,ignore_index=True,sort=False)

    blob_data.shape
    blob_data_shuffled = blob_data.sample(frac=1).reset_index(drop=True)
    if trainSamples >= len(blob_data_shuffled):
        print("Requested more images than available!")
        trainSamples = len(blob_data_shuffled)

    return blob_data_shuffled.head(trainSamples)


