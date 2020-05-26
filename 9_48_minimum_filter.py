#make image softer
from PIL import Image
import scipy.ndimage as sc
import scipy.misc as sm

a = Image.open('images/lena512.bmp')

b = sc.filters.minimum_filter(a, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

b = Image.fromarray(b)

b.show()