from skimage import io as io
from skimage.filters import gabor
from skimage import data

from matplotlib import pyplot as plt 

image = data.coins()

filt_real, filt_imag = gabor(image, frequency=0.6)

plt.figure()

io.imshow(filt_real)
io.show()
