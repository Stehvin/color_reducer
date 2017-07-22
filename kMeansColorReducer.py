# -*- coding: utf-8 -*-
import pdb
import scipy as sp
import numpy as np
from random import sample


# set file path for image
picFile = r"C:\Users\Stehvin\Pictures\Chicago.jpg"

# choose K (num colors), max centroid iterations, and number of runs
k = 3
maxIter = 20
numRuns = 50

def imageToMatrix(imageFilePath):
    """Convert an image into an m x 3 matrix, where m is the total
    number of pixels in the image, and the 3 columns represent each
    pixel's RGB values.
    """
    # load image as matrix
    picMatrix = sp.misc.imread(picFile)

    # change picture matrix from 3D to 2D
    # (pixels are rows, RGB values are columns)
    matrix2D = np.reshape(picMatrix, (-1, picMatrix.shape[-1]))
    return matrix2D

def randomCen(matrix2D, k):
    """Randomly initialize k centroids.
    Given a 2D picture matrix, this function randomly picks k number 
    of rows to assign to the centroids matrix.
    
    Example
    ------
    matrix2D -> 500 x 3
    k = 4
    centroids -> 4 x 3
    """
    randIndicies = sample(range(0, matrix2D.shape[0]), k)
    centroids = np.zeros((k, matrix2D.shape[1]))
    for i in range(0, k):
        centroids[i,:] = matrix2D[randIndicies[i],:]
    return centroids

def closestCen(matrix2D, centroids):
    """Assign every pixel in matrix2D to its closest centroid.
    
    Parameters
    ---------
    matrix2D: numpy array
        2D matrix (m x 3) representing a picture.
    centroids: numpy array
        2D matrix (k x 3) representing centroid locations.
        
    Returns
    ---------
    indicies: numpy array
        Vector (m x 1) representing which centroid is closest
        to each pixel.
    cost: float
        The total cost (distance squared) of current centroid 
        assignments.
    """
    # initialize variables    
    m = matrix2D.shape[0]
    k = centroids.shape[0]    
    distMatrix = np.zeros([m, k])
    indicies = np.zeros([m, 1])
    
    # loop over centroids
    for i in range(k):
        
        # find distance from every pixel to centroid
        diffMatrix = matrix2D - centroids[i, :]
        distMatrix[:, i] = np.sum(diffMatrix**2, axis=1)
    
    # save each pixel's closest centroid in indicies vector
    indicies = np.argmin(distMatrix, axis=1)
    cost = (1 / m) * np.sum(np.min(distMatrix, axis=1))
    return indicies, cost

# move centroids function
'''
def moveCen(assignedPoints, centroids):
    return centroids
'''

# function to run K-Means
'''
def runKMeans(pictureArray, centroids, maxIter)
    return centroids, cost
'''

# run K-Means numRuns times
'''
for i in range(numRuns):
    centroids = randomCen(pictureArray)
    centroids, cost = runKMeans(pictureArray, centroids, maxIter)
    
    if cost < smallcost:
        bestCen = centroids
        bestPoints = closestCen(pictureArray, bestCen)

'''

# convert array back into image, then output

pdb.set_trace()
matrix2D = imageToMatrix(picFile)
centroids = randomCen(matrix2D, k)
indicies, cost = closestCen(matrix2D, centroids)


