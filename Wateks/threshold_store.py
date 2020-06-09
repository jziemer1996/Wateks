# ------------------------------------THRESHOLD STORE MODULE--------------------------------------- #

# Module to store threshold functions used in water_functions.py and binary_functions.py.

# ------------------------------------------------------------------------------------------------- #

##############################     IMPORT OF REQUIRED MODULES    ###################################

from skimage import io
from skimage.filters import *

##############################     THRESOLD FUNCTIONS STORE      ###################################

input_folder = "D:/HiWi/01_SALDI/Output_Mpumalanga/"
input_tif = "Driekoppies_VH_median_filter3_threshold_otsu5"
input = input_folder+input_tif
image = io.imread(input)
thresh_otsu = threshold_otsu(image)
thresh_triangle = threshold_triangle(image)
thresh_mean = threshold_mean(image)
thresh_minimum = threshold_minimum(image)
thresh_li = threshold_li(image)
thresh_yen = threshold_yen(image)