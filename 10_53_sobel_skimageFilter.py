from PIL import Image
from skimage import filters
import scipy 

a = Image.open('images/moon.jpg')

b = filters.sobel(a)
b = Image.fromarray(b)

b.show()
