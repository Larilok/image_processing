from PIL import Image
from pylab import *

img = Image.open('images/profile.jpg').convert('L')

print(array(img)[500])
imgArray = array(img)

figure()
hist(imgArray.flatten(), 300)
show()
# img.show()
