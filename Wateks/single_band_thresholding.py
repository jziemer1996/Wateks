"""
============
Thresholding
============

Thresholding is used to create a binary image from a grayscale image [1]_.

.. [1] https://en.wikipedia.org/wiki/Thresholding_%28image_processing%29

.. seealso::
    A more comprehensive presentation on
    :ref:`sphx_glr_auto_examples_applications_plot_thresholding.py`

"""


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
from Wateks.main_module import *


######################################################################
# We illustrate how to apply one of these thresholding algorithms.
# Otsu's method [2]_ calculates an "optimal" threshold (marked by a red line in the
# histogram below) by maximizing the variance between two classes of pixels,
# which are separated by the threshold. Equivalently, this threshold minimizes
# the intra-class variance.
#
# .. [2] https://en.wikipedia.org/wiki/Otsu's_method
#
### Bei einfachem Ausführen des Moduls muss nichts auskommentiert werden
### Bei komplexem Ausführen über water_functions.py Histogramme und print-Funktion auskommentieren

image = io.imread("D:/HiWi/01_SALDI/Output_Mpumalanga/Driekoppies_VH_median_filter3_threshold_li7")
thresh = threshold_li(image)

binary = image < thresh

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

print("threshold of separation = " + str(thresh))
