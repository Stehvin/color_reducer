# -*- coding: utf-8 -*-
import pdb
import scipy as sp
import numpy as np
from random import sample
import math


# set file path for image
picFile = r"C:\Users\Stehvin\Pictures\Chicago.jpg"

# choose K (num colors), max centroid iterations, and number of runs
k = 3
maxIter = 10
numRuns = 4

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

def moveCen(matrix2D, indicies, k):
    """Move each centroid to the average value of all pixels 
    assigned to the centroid.
    """
    # initialize centroid matrix
    centroids = np.zeros([k, 3])
    
    # get total number of pixels assigned to each centroid
    cenCount = np.bincount(indicies)
    
    # loop over centroids
    for i in range(k):
        
        # create boolean array showing which pixels are
        # assigned to the ith centroid (m x 1)
        boolVec = np.array([indicies == i]).T
        
        # broadcast multiply matrix2D and boolVec to remove all
        # pixels not assigned to this function
        centroidPixels = matrix2D * boolVec
        centroids[i, :] = \
            np.sum(centroidPixels, axis=0) / cenCount[i]
    
    return centroids


# function to run K-Means
def runKMeans(matrix2D, k, maxIter):
    """Runs K-Means algorithm.
    The centroids will be updated "maxIter" times.
    """
    # randomly generate initial centroids    
    centroids = randomCen(matrix2D, k)
    
    # run K-means algorithm    
    for i in range(maxIter):
        indicies, cost = closestCen(matrix2D, centroids)
        centroids = moveCen(matrix2D, indicies, k)
    return centroids, cost

def execute(matrix2D, k, maxIter, numRuns):
    """Runs the whole K-means algorithm "numRuns" number of times.
    The centroids with the lowest cost will be chosen as the final
    centroids, and each pixel will be assigned to its closest
    final centroid.
    """
    # initialize lowcost to infinity
    lowcost = math.inf
    
    for i in range(numRuns):
        centroids, cost = runKMeans(matrix2D, k, maxIter)
        if cost < lowcost:
            bestCen = centroids
    
    bestIndicies = closestCen(matrix2D, bestCen)[0]
    return bestCen[bestIndicies, :]

# convert array back into image, then output

#pdb.set_trace()
matrix2D = imageToMatrix(picFile)
what = execute(matrix2D, k, maxIter, numRuns)
print(what)


