import math,numpy
import scipy.misc
from PIL import Image

a = Image.open('images/girlface.bmp')
b = numpy.asarray(a)
print(b)
gamma = 0.5

b1 = b.astype('float')
b3 = numpy.max(b1)
# values now between 0 and 1
b2 = b1/b3
b3 = numpy.log(b2) * gamma
c = numpy.exp(b3)*255.0 #gamma correction
c1 = c.astype('int')
d = Image.fromarray(c1)
d.show()
