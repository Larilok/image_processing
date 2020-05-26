#a sort of a blur filter

from PIL import Image
import scipy.ndimage as sc
import numpy as np

a = Image.open('images/lena_noisy.png').convert('L')

k = np.ones((5,5))/25

b = sc.filters.convolve(a,k)
b = Image.fromarray(b)
b.show()
# b.save('images/profile_mean.jpg')
