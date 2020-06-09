# -------------------------------SINGLE BAND THRESHOLDING MODULE----------------------------------- #

# Module for the detection of water in one image (binary analysis).
# Execute this script as stand alone!
# ------------------------------------------------------------------------------------------------- #

##############################     IMPORT OF REQUIRED MODULES    ###################################

import collections

import matplotlib.pyplot as plt
import skimage
from skimage import data
from skimage.filters import *
from skimage import io
import rasterio as rio
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import _collections

########################################     INPUT    ##############################################

input_folder = "F:/HiWi/01_SALDI/Output_Mpumalanga/"
input_tif = "Driekoppies_VH_median_filter3_threshold_otsu5_binary_otsu17"
input = input_folder+input_tif
image = io.imread(input)
thresh = threshold_triangle(image)

######################################     HISTOGRAM    ############################################

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 2, 1)
ax[1] = plt.subplot(1, 2, 2)

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

plt.show()

###################################     CLASSIFICATION REPORT    ###################################

# Number of pixels on x_axis
x_axis_len = image.shape[1]  # length of x-axis
# Number of pixels on y_axis
y_axis_len = image.shape[0]  # length of y-axis
# Number of pixels in array
sum = x_axis_len * y_axis_len


print("Number of non-water-pixels in image = ")
number_of_zeroes = np.count_nonzero(image == 0)
print(number_of_zeroes)
print((number_of_zeroes/sum)*100, "%")

print("Number of water-pixels in image = ")
number_of_water = np.count_nonzero(image == 1)
print((number_of_water/sum)*100, "%")
print(number_of_water)

print("threshold of separation = " + str(thresh))
