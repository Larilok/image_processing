import numpy as np
from matplotlib import cm
from PIL import Image
from pylab import *

x = np.random.randint(0,255,(300,300)).astype('uint8')

subplot(1,2,1)
plt.imshow(x, cmap=cm.gray)
plt.title('gray random')

y = np.random.randint(0,255,(300,400, 3)).astype('uint8')
subplot(1,2,2)
plt.imshow(y)
plt.title('colored random')
plt.show()
