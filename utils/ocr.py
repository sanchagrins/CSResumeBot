# -*- coding: utf-8 -*-
import os
import pytesseract
from PIL import Image
import mkdir

def scan(img, inputDir):
    directory = './scanned'
    mkdir.make(directory)
    filename = img.split(".")
    filename = filename[0:].append(".txt")
    f = open(directory + str(filename),'w')
    f.write(pytesseract.image_to_string(Image.open(inputDir + img)))


directory = './filtered/'
for img in os.listdir(directory):
        scan(img, directory)
