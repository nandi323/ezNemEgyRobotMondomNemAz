import cv2
import numpy as np
import sklearn

src_path = 'C:\\Users\\balint.nandor\\Documents\\ezNemEgyRobotMondomNemAz\\DofusMovement\\analyze\\noisefree\\kurva.bmp'

samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE,responses)

im = cv2.imread(src_path)

out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

_, contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>7:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>3 and w<50:
            # cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
            print(chr(results))
            string = str(chr((results[0][0])))
            cv2.putText(out,string,(x,y+h),16,0.5,(0,255,0))

imBig = cv2.resize(im,(900,140))
cv2.imshow('im',imBig)
outBig = cv2.resize(out,(900,140))
cv2.imshow('out',outBig)
cv2.waitKey(0)