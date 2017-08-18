# -*- coding: utf-8 -*-
import os

import mkdir
from PIL import Image
from PIL import ImageFilter

def imageFilter(img):
    img_file = './img/' + img
    im = Image.open(img_file)
    width, height = im.size
    print(width)
    size = width * 3, height * 3
    print(size)
    im = im.resize(size, Image.BICUBIC)
    print(im.size)
    im = im.filter(ImageFilter.SHARPEN)
    path = './filtered'
    mkdir.make(path)
    filename = 'filtered_' + img
    if 'jpg' in img:
        im = im.convert("RGB")
    im.save(os.path.join(path, filename))

directory = './img/'
for img in os.listdir(directory):
    imageFilter(img)
