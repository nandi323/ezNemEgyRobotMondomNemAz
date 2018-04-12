import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from sklearn import svm

src_path = 'C:/Users/balint.nandor/Documents/ezNemEgyRobotMondomNemAz/DofusMovement/analyze/'

# imgName = src_path + filename
#
# image = cv2.imread(imgName, 0)
#
# # convert image black and white
# thresh, im_bw = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
#
# cv2.imshow("alma",im_bw)
#
# imageArray = np.asarray(im_bw)
#
# plt.imshow(imageArray)
# plt.show()
for file in os.listdir(src_path):
    if file.endswith(".png"):
        img = cv2.imread(file, 0)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        print(file)
        # Write image after removed noise
        cv2.imwrite(src_path + 'noisefree/' + file.split('.png')[0]  + '_removed_noise.jpg', img)



