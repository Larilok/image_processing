from PIL import Image
import os

imagesPathToConvert = ['images/profile.jpg', 'images/moon.png']

for imagePath in imagesPathToConvert:
  outfile = imagePath.split('.')[0]+"T.tiff"
  if imagePath != outfile:
    Image.open(imagePath).save(outfile)