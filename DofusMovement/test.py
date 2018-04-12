from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np

src_path = 'C:/Users/Kapi/Documents/GitHub/ezNemEgyRobotMondomNemAz/DofusMovement/analyze/noisefree/test/'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

print(pytesseract.image_to_string(Image.open('analyze/noisefree/test/alma.jpg')))