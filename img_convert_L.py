from PIL import Image

img = Image.open('./images/profile.jpg').convert('L')
img.save('./images/profileL.jpg')