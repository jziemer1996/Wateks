# -----------------------------------BINARY FUNCTIONS MODULE--------------------------------------- #

# Module for the detection of water in one image (binary analysis).
# To make use of the functionality implemented in this module, first execute water_functions.py!

# ------------------------------------------------------------------------------------------------- #

def binary_otsu(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_otsu
    if thresh_otsu < arr1d:
        return 0
    if thresh_otsu > arr1d:
        return 1


def binary_triangle(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_triangle
    if thresh_triangle < arr1d:
        return 0
    if thresh_triangle > arr1d:
        return 1


def binary_mean(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_mean
    if thresh_mean < arr1d:
        return 0
    if thresh_mean > arr1d:
        return 1


def binary_minimum(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_minimum
    if thresh_minimum < arr1d:
        return 0
    if thresh_minimum > arr1d:
        return 1


def binary_li(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_li
    if thresh_li < arr1d:
        return 0
    if thresh_li > arr1d:
        return 1


def binary_yen(arr1d):
    from skimage import io
    from Wateks.threshold_store import thresh_yen
    if thresh_yen < arr1d:
        return 0
    if thresh_yen > arr1d:
        return 1