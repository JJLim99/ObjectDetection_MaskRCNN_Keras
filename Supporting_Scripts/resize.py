from PIL import Image
import os, sys

# Path to the targeted directory
path = "D:/AI_Project/dataset/test/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # Resize images (width, height)
            imResize = im.resize((800,600), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()