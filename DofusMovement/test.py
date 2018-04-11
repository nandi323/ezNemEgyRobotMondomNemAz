from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np

with open("onlyResources.txt", 'r') as inFile:
    for line in inFile:
        itemName = line