from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *
from skimage import data

scanned = data.page()
#scanned = np.array(Image.open('images/moon.png')).astype('uint8')
print(scanned[0][21])
thres = np.zeros(shape(scanned)).astype('uint8')
for line in range(len(scanned)):
  for pixel in range(len(scanned[0])):
      #left part of image
      if pixel < 200:
          #down corner
          if line > 140 and pixel < 40:
              if scanned[line][pixel] >= 63:
                thres[line][pixel] = 255
          else:
              if scanned[line][pixel] >= 80:
                thres[line][pixel] = 255
        #right part
      else:
          if scanned[line][pixel] >= 150:
            thres[line][pixel] = 255


#thres[scanned < threshold] = 0
#thres[scanned >= threshold] = 255
#print(thres[25])
plt.imshow(thres, cmap=cm.gray)

#plt.imsave('images/binary.jpg', thres, cmap=cm.gray)
plt.show()
