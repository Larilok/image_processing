import numpy as np 
import scipy.misc, math
from PIL import Image
from pylab import *

img = Image.open('images/lena512.bmp')
img1 = array(img)
fl = img1.flatten()

figure()
hist(fl, 300)

hiss, bins = np.histogram(img1, 256, [0,255])
cdf = hiss.cumsum()
cdfNoZeroes = np.ma.masked_equal(cdf, 0)

#min value in no 0 is now 0 :) and expanded by 255
numrtr_CdfNoZeroes = (cdfNoZeroes - cdfNoZeroes.min())*255 
denomntr_CdfNoZeroes = (cdfNoZeroes.max() - cdfNoZeroes.min())
#magic done and values normalized
cdfNoZeroes = numrtr_CdfNoZeroes / denomntr_CdfNoZeroes

cdf = np.ma.filled(cdfNoZeroes, 0).astype('uint8')

im2 = cdf[fl]
im3 = np.reshape(im2, img1.shape)
im4 = Image.fromarray(im3)
img4 = array(im4)
fl=img4.flatten()

figure()
hist(fl, 300)

im4.show()
show()
