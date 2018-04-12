import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from PIL import Image
import time
from sklearn import svm
from sklearn import datasets

src_path = 'C:/Users/Kapi/Documents/GitHub/ezNemEgyRobotMondomNemAz/DofusMovement/analyze/noisefree/test/'

dataset = []
resultset = []

for file in os.listdir(src_path):
    if file.endswith(".jpg"):
        image = cv2.imread(src_path + file, 0)
        # convert image black and white
        thresh, im_bw = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

        imageArray = np.asarray(im_bw)

        dataset.append(imageArray)

numpyArray = np.array(dataset)

# with open('imagesInArrayFormat.txt', 'w') as outfile:
#     # I'm writing a header here just for the sake of readability
#     # Any line starting with "#" will be ignored by numpy.loadtxt
#     # outfile.write('# Array shape: {0}\n'.format(numpyArray.shape))
#
#     # Iterating through a ndimensional array produces slices along
#     # the last axis. This is equivalent to data[i,:,:] in this case
#     for data_slice in numpyArray:
#
#         # The formatting string indicates that I'm writing out
#         # the values in left-justified columns 7 characters in width
#         # with 2 decimal places.
#         np.savetxt(outfile, data_slice)
#
#         # Writing out a break to indicate different slices...
#         # outfile.write('# New slice\n')
# outfile.close()


# newData = np.loadtxt('imagesInArrayFormat.txt')
# alma = np.array(newData.reshape(len(dataset),16,90))

# plt.imshow(alma[1])
# plt.show()
#
# for data in dataset:
#     plt.imshow(data)
#     plt.show()
#     szam = input("add meg a kepen lathato szamot : ")
#     resultset.append(szam)
#     plt.close()
#
# np.save('resultDataset', resultset)

np.set_printoptions(threshold=np.nan)
clf = svm.SVC(gamma=0.001, C=100)
x = np.loadtxt('imagesInArrayFormat.txt')
alma = np.array(x.reshape(len(dataset),16,90))
digit = datasets.load_digits()

flatim = alma.flatten()

X = alma.reshape(14,1440)
y = np.load("resultDataset.npy")

clf.fit(X,y)

print('predict', clf.predict(X))

