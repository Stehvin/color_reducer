# Color-Limited Sketch / JPEG Color Reducer
This program intelligently reduces the number of colors in a JPEG image. Here, "intelligently" means the program considers all the colors in the original image and tries to choose output colors that are closest to those original colors. For example, say a picture of a lake surrounded by forest was input into the program, and the user wanted the output image to have only two colors. The program would likely choose blue and green as its two colors, since the lake portion of the image is dominated by blues and the forest portion is dominated by greens.

# How it Works
This is accomplished using a k-means clustering algorithm. All of the pixels in the original image have three parameters, their red, green, and blue (RGB) color values. When the user chooses *k* (the number of colors for the output image), *k* centroids are generated with random RGB values. The program then completes ten iterations through the k-means algorithm, where, in each iteration, all the pixels are assigned to their closest centroid, and then all of the centriods move to the average position of the pixels assigned to them. Once one "run" (ten iterations) of the k-means algorithm is complete, the program does nine more runs, generating new randomly-chosen centroids at the beginning of each run. The centroids with the lowest cost (determined by the sum of each pixel's distance from its centriod) are chosen as the colors for the final image. Finally, all pixels assigned to each centroid are given the RGB values of their centroid and outputted into the final picture.

# How to Use the GUI (Graphical User Interface)
An executable version (.exe file) of this program can be downloaded at this [link](https://drive.google.com/open?id=0BwsPnrvZsDI-Z3pudjlOeERPNjQ). Running this .exe file will start the GUI. The user must input a file path to a JPEG image, the desired file path for the output image, and the number of colors they would like to use for the output image.

Note: Due to the program's use of a k-means clustering algorithm, processing time will increase with the size of the image and the number of colors chosen. Users who are waiting for an excessive amount of time should try using a smaller picture or choosing a smaller number of colors.

# Files in this Repository
### sklearnColorReducer.py
Implementation of the k-means clustering algorithm, using the scikit-learn module. This implementation is significantly faster than the kMeansColorReducer.py implementation.

### colorReducerGUI.py
Graphical user interface (GUI) for Color-Limited Sketch program. GUI can be opened by running the executable file linked above. Uses multi-threading to keep itself responsive while simultaneously running the k-means algorithm (via sklearnColorReducer.py).

### kMeansColorReducer.py
Implementation of the k-means clustering algorithm without using scikit-learn. This file was completed for fun and is not used in the executable version of this program.
