from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np
import sys
import os

import cv2
import matplotlib.pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
from skimage.feature import hog

src_path = 'C:\\Users\\balint.nandor\\Documents\\ezNemEgyRobotMondomNemAz\\DofusMovement\\analyze\\noisefree\\test\\'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

for file in os.listdir(src_path):
    if file.endswith(".bmp"):
        im = cv2.imread(src_path + file)
        print(file)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

        _, contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        samples = np.empty((0,100))

        responses = []
        keys = [i for i in range(256)]

        for cnt in contours:
            if cv2.contourArea(cnt)>7:
                [x,y,w,h] = cv2.boundingRect(cnt)
                print(x,y,w,h)
                if  h>3 and w<20:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                    roi = thresh[y:y+h,x:x+w]
                    roismall = cv2.resize(roi,(10,10))
                    cv2.imshow('norm',im)
                    imBig = cv2.resize(im,(900,140))
                    cv2.imshow("big",imBig)
                    key = cv2.waitKey(0)
                    # print(key)
                    # print(chr(key))
                    if key == 27:  # (escape to quit)
                        sys.exit()
                    elif key in keys:
                        print(chr(key))
                        responses.append(key)
                        sample = roismall.reshape((1,100))
                        samples = np.append(samples,sample,0)

        responses = np.array(responses)
        responses = responses.reshape((responses.size,1))
        print ("training complete" , file)

        np.savetxt('generalsamples.data',samples)
        np.savetxt('generalresponses.data',responses)
