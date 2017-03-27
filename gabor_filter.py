from skimage import io as io
from skimage.filters import gabor
from skimage import data
from skimage.util import img_as_float

from scipy import ndimage as ndi

import numpy as np

from matplotlib import pyplot as plt 

import cv2

def build_filters():
    filters = collections.OrderedDict()
    gamma = 0.3
    for (ksi, ksize, lam) in ((3, 5, 0.8), (5, 5, 1.6), 
                                 (7, 5, 2.4), (9, 5, 3.2), 
                                 (11, 7, 1.6), (13, 7, 2.4), 
                                 (15, 7, 3.2), (17, 7, 4.0), 
                                 (19, 11, 2.4), (21, 11, 3.2), 
                                 (23, 11, 4.0), (25, 11, 4.8), 
                                 (27, 15, 3.2), (29, 15, 4.0)):
            sigma = 0.8 * lam
            i=0
            for theta_degrees in (0., 22.5, 45., 67.5, 90., 112.5, 135., 157.5):
                theta = theta_degrees * np.pi / 180.
                
                i=i+1
                indexName = "A" + str(i) + "S" + str(ksi)
                
                if(useOpenCV == 1):
                    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lam, gamma, 0, ktype=cv2.CV_32F)
                    kernel /= 1.5*kernel.sum()
                else:
                    kernel = gabor_kernel(lam, theta=theta, sigma_x=sigma, sigma_y=sigma)
                filters[indexName] = kernel
        return filters

