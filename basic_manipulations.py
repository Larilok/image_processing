from PIL import Image

img = Image.open('images/pens.bmp')

smaller_img = img.crop((0,150,350,450)).resize((10000,10000)).rotate(-270)
smaller_img.save('enormous_pen.jpg')