# ----------------------------------------WATER FUNCTIONS MODULE----------------------------------- #

# Module for the detection of water extent over time (non-binary analysis).
# Precondition to execute binary_functions.py.

# ------------------------------------------------------------------------------------------------- #

##############################     IMPORT OF REQUIRED MODULES    ###################################

import skimage
import skimage.filters as sf
from skimage.filters import *
from scipy.signal import find_peaks

################################     WORKING FUNCTIONS     #########################################

def count_abs_peak(arr1d, threshold):
    """
        calculates the number of scenes which are underflooded depending on the peak count function which
        calculates how often the signal drops beneath a certain threshold
        ----------
        arr1d: numpy.array
            1D array representing the time series for one pixel
        threshold: float
            radar backscatter value - depends on type of polarization (smaller for VH than for VV)

        Returns
        ----------
        numpy.int32
            returns the number of how often the radar signal drops beneath a certain threshold
    """
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=threshold)
    return len(peaks)


def count_interval_peak(arr1d, lower, upper):
    """
        calculates the number of scenes which are underflooded depending on the peak count function which
        calculates how often the signal drops beneath a certain threshold interval
        ----------
        arr1d: numpy.array
            1D array representing the time series for one pixel
        lower: float
            lower radar backscatter value - depends on type of polarization (smaller for VH than for VV)
        upper: float
            Upper radar backscatter value - depends on type of polarization (smaller for VH than for VV)

        Returns
        ----------
        numpy.int32
            returns the number of how often the radar signal drops beneath a certain threshold
    """
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=(lower, upper))
    return len(peaks[0])


def count_abs_index(arr1d, threshold):
    """
        calculates the total number of scenes which are underflooded depending on an certain threshold considering the
        total number of available scenes
        ----------
        arr1d: numpy.array
            1D array representing the time series for one pixel
        threshold: float
            radar backscatter value - depends on type of polarization (smaller for VH than for VV)

        Returns
        ----------
        numpy.int32
            returns the number of total scenes which are inundated in the time series stack
    """
    count = 0
    for ele in arr1d:
        if ele <= threshold:
            count = count + 1
    return count


def count_interval_index(arr1d, lower, upper):
    """
        calculates the total number of scenes which are underflooded depending on an threshold interval considering the
        total number of available scenes
        ----------
        arr1d: numpy.array
            1D array representing the time series for one pixel
        lower: float
            lower radar backscatter value - depends on type of polarization (smaller for VH than for VV)
        upper: float
            Upper radar backscatter value - depends on type of polarization (smaller for VH than for VV)

        Returns
        ----------
        numpy.int32
            returns the number of total scenes which are inundated in the time series stack
    """
    count = 0
    for ele in arr1d:
        if ele >= lower and ele <= upper:
            count = count + 1
    return count


def threshold_otsu(arr1d):
    """
    https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_otsu
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_otsu(arr1d, nbins=256)
    #print(thresh)
    return thresh


def threshold_li(arr1d):
    """
    works with errors
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_li(arr1d, tolerance=None,
                             initial_guess=None, iter_callback=None)
    return thresh


def threshold_yen(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_yen(arr1d, nbins=256)
    return thresh


def threshold_mean(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_mean(arr1d)
    return thresh


def threshold_triangle(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_triangle(arr1d, nbins=256)
    return thresh


def threshold_median(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import numpy as np
    thresh = np.median(arr1d)
    return thresh

##############################     NON-WORKING FUNCTIONS     #######################################

def threshold_local(arr1d):
    """
    doesnt work because its no 2D array
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_local(arr1d, block_size=9, method='gaussian',
                                offset=0, mode='reflect')
    return thresh


def threshold_minimum(arr1d):
    """
    doesnt work: Unable to find two maxima in histogram
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_minimum(arr1d, nbins=256, max_iter=100)
    return thresh


def threshold_niblack(arr1d):
    """
    doesnt work: TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_niblack(arr1d, window_size=15, k=0.2)
    return thresh


def threshold_sauvola(arr1d):
    """
    doesnt work: TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_sauvola(arr1d, window_size=15, k=0.2, r=None)
    return thresh


def threshold_multiotsu(arr1d, classes):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_multiotsu(arr1d, classes, nbins=256)
    return thresh


def apply_hysteresis_threshold(arr1d):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.apply_hysteresis_threshold(arr1d, low=-25.0, high=-23.0)
    return thresh


def unsharp_mask(arr1d):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.unsharp_mask(arr1d, radius=1.0, amount=1.0, multichannel=False,
                             preserve_range=False)
    return thresh

################################    LETS GIVIT A TRY FUNCTIONS    ##################################

def inverse(arr1d):
    import skimage.filters as sf
    skimage.filters.inverse(arr1d, impulse_response=None,
                        filter_params={}, max_gain=2, predefined_filter=None)

def try_all_threshold(arr1d):
    import skimage.filters as sf
    skimage.filters.try_all_threshold(arr1d, figsize=(8, 5), verbose=True)