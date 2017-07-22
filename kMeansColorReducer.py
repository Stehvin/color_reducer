# -*- coding: utf-8 -*-

import scipy as sp
import numpy as np
from random import sample

# Load image as matrix
picFile = "C:/Users/blah/foo/bar.jpg"
picMatrix = sp.misc.imread(picFile)

# Change picture matrix from 3D to 2D
# (pixels are rows, RGB values are columns)
matrix2D = np.reshape(picMatrix, (-1, picMatrix.shape[-1]))

# Choose K (num colors), max centroid iterations, and number of runs
k = 3
maxIter = 20
numRuns = 50

# Randomly initialize k centroids function
def randomCen(matrix2D):
    randIndicies = sample(range(0, matrix2D.shape[0]), k)
    centroids = np.zeros((k, matrix2D.shape[1]))
    for i in range(0, k):
        centroids[i,:] = matrix2D[randIndicies[i],:]
    return centroids

# Point/cluster assignment function
'''
    def closestCen(pictureArray, centroids):
        return assignedPoints
'''
        
# Move centroids function
'''
    def moveCen(assignedPoints, centroids):
        return centroids
'''

# Function to run K-Means
'''
    def runKMeans(pictureArray, centroids, maxIter)
        return centroids, cost
'''

# Run K-Means numRuns times
'''
    for i in range(numRuns):
        centroids = randomCen(pictureArray)
        centroids, cost = runKMeans(pictureArray, centroids, maxIter)
        
        if cost < smallcost:
            bestCen = centroids
            bestPoints = closestCen(pictureArray, bestCen)

'''

# Convert array back into image, then output

