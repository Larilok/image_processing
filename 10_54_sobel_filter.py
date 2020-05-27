from skimage import img_as_int
import cv2
import numpy as np
from pylab import *
import scipy.ndimage.filters as filters

#img = cv2.imread('images/profile.jpg', 0)
img = cv2.imread('images/moon.jpg',0)

sobel_operator_v = np.array([
  [-1, 0, 1],
  [-2, 0 ,2],
  [-1, 0, 1]
])

sobelX = cv2.Sobel(img, -1, 1, 0, ksize=5)
sobelY = cv2.Sobel(img, -1, 0, 1, ksize=5)

subplot(2,2,1)
plt.imshow(sobelX, cmap='gray')
plt.title('(-1, 1, 0)')

subplot(2,2,2)
plt.imshow(sobelY, cmap='gray')
plt.title('(-1, 0, 1)')

subplot(2,2,3)
plt.imshow(filters.convolve(img_as_int(img), sobel_operator_v), cmap='gray')
plt.title('sobel vertical')

subplot(2,2,4)
plt.imshow(filters.convolve(img_as_int(img), sobel_operator_v.T), cmap='gray')
plt.title('sobel horizontal')

plt.show()
