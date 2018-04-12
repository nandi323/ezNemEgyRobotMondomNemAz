from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np

alma = np.load("resultDataset.txt.npy")

print(alma)