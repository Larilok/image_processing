from PIL import Image
from skimage import img_as_int
import cv2
import numpy as np
from pylab import *
import scipy.ndimage.filters as filters

img = cv2.imread('images/profile.jpg', 0)
#img = cv2.imread('images/moon.jpg',0)

laplacian_operator_pos = np.array([
  [0, -1, 0],
  [-1, 4 ,-1],
  [0, -1, 0]
])

laplacian_operator_neg = np.array([
  [0, 1, 0],
  [1, -4 ,1],
  [0, 1, 0]
])

laplacian_neg = cv2.Laplacian(img, -1)

subplot(1,3,1)
plt.imshow(laplacian_neg, cmap='gray')
plt.title('filter neg')

subplot(1,3,2)
plt.imshow(filters.convolve(img_as_int(img), laplacian_operator_pos), cmap='gray')
plt.title('operator pos')

subplot(1,3,3)
plt.imshow(filters.convolve(img_as_int(img), laplacian_operator_neg), cmap='gray')
plt.title('operator neg')



plt.show()
