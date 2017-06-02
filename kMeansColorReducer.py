# -*- coding: utf-8 -*-

'''
Load image

Convert image to RGB matrix (3D or 4D)

Choose K (num colors), max centroid iterations, and number of runs
    k = 3
    maxIter = 20
    numRuns = 50

Randomly initialize k centroids function
    def randomCen(pictureArray)
        return centroids = []

Point/cluster assignment function
    def closestCen(pictureArray, centroids):
        return assignedPoints
        
Move centroids function
    def moveCen(assignedPoints, centroids):
        return centroids

Function to run K-Means
    def runKMeans(pictureArray, centroids, maxIter)
        return centroids, cost

Run K-Means numRuns times
    for i in range(numRuns):
        centroids = randomCen(pictureArray)
        centroids, cost = runKMeans(pictureArray, centroids, maxIter)
        
        if cost < smallcost:
            bestCen = centroids
            bestPoints = closestCen(pictureArray, bestCen)

Convert array back into image, then output
'''