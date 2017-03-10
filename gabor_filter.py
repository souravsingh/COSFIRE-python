import numpy as np

from skimage import io as io
from skimage.filters import gabor
from skimage import data

from matplotlib import pyplot as plt 

np.random.seed(42)

image = data.coins()

filt_real, filt_imag = gabor(image, frequency=0.6)

plt.figure()

io.imshow(filt_real)
io.show(0
