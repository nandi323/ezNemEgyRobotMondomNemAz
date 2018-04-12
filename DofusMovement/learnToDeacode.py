import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time
from sklearn import svm

src_path = 'C:/Users/balint.nandor/Documents/ezNemEgyRobotMondomNemAz/DofusMovement/analyze/noisefree/'

for file in os.listdir(src_path):
    if file.endswith(".jpg"):
        image = cv2.imread(src_path + file, 0)
        print(file)
        # convert image black and white
        thresh, im_bw = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

        cv2.imshow("alma",im_bw)

        imageArray = np.asarray(im_bw)

        plt.imshow(imageArray)
        plt.show()
        time.sleep(4)


