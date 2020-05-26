from PIL import Image
from pylab import *

im = array(Image.open('images/profile.jpg').convert('L'))

#Convert to negative
im2 = 255 - im
negative = Image.fromarray(im2)
#negative.show()

#Interval 100..200
im3 = (100.0/255) * im + 100
interval = Image.fromarray(im3)
#interval.show()

#Square image
im4 = 255.0 * (im/255.0) ** 2
squared = Image.fromarray(im4)
squared.show()

