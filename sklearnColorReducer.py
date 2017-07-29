# Author: Stehvin Olson

import numpy as np
import scipy as sp
import sklearn

def main():
    # set input and output file paths for image
    inputFile = r"C:\Users\Stehvin\Pictures\casey cody.jpg"
    outputFile = r"C:\Users\Stehvin\Pictures\kMeans\caseyCody10k.jpg"
    
    # choose K (num colors), max centroid iterations, and number of runs
    k = 10
    maxIter = 10
    numRuns = 10
    
    # create 2D picture matrix
    matrix2D = imageToMatrix(inputFile)
    
    # run K-means to assign every pixel to one of "k" colors
    kColorsMatrix = execute(matrix2D, k, maxIter, numRuns)
    
    # assign each pixel to its closest centroid
    
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
    
if __name__ == "__main__":
    main()