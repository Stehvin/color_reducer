# Author: Stehvin Olson

import numpy as np
import scipy as sp
from sklearn.cluster import KMeans

def execute(inputFile, outputFile, k):   
    # choose max centroid iterations and number of runs
    maxIter = 10
    numRuns = 10
    
    # create 2D picture matrix
    matrix2D = imageToMatrix(inputFile)
    
    # run K-means
    kMeans = KMeans(n_clusters=k, n_init=numRuns, max_iter=maxIter)
    kMeans.fit(matrix2D)
    centroids = kMeans.cluster_centers_
    indicies = kMeans.labels_
    
    # assign each pixel to its closest centroid
    kColorsMatrix = centroids[indicies, :]
    
    # convert pixel matrix back into image, then save to output file
    img = kColorsMatrix.reshape(sp.misc.imread(inputFile).shape)
    sp.misc.imsave(outputFile, img)

def imageToMatrix(imageFilePath):
    """Convert an image into an m x 3 matrix, where m is the total
    number of pixels in the image, and the 3 columns represent each
    pixel's RGB values.
    """
    # load image as matrix
    picMatrix = sp.misc.imread(imageFilePath)

    # change picture matrix from 3D to 2D
    # (pixels are rows, RGB values are columns)
    matrix2D = np.reshape(picMatrix, (-1, picMatrix.shape[-1]))
    return matrix2D