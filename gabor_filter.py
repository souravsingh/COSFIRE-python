from skimage import io as io
from skimage.filters import gabor
from skimage import data
from skimage.util import img_as_float

from scipy import ndimage as ndi

import numpy as np

from matplotlib import pyplot as plt 

def build_filters():
    filters = []
    ksize = 9
    for theta in range(0, 8):
        theta = theta / 4. * np.pi
        for lamda in np.arange(0, np.pi, np.pi/4): 
            kern = cv2.getGaborKernel((ksize, ksize), 1.0, theta, lamda, 0.5, 0, ktype=cv2.CV_32F)
            kern /= 1.5*kern.sum()
            filters.append(kern)
    return filters


