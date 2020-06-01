import Pillow

img = Image.open('h.jpg')
box = (0, 0, 75, 75)
region = img.crop(box)
