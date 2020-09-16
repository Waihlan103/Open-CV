import cv2 as cv
import numpy as np

def click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv.FONT_HERSHEY_SIMPLEX
        pt = str(x)+','+str(y)
        cv.putText(img, pt, (x, y), font, .5, (0, 0, 255), 2)
        cv.imshow('image', img)

img = cv.imread('beckham.jpg')
cv.imshow('image', img)
cv.setMouseCallback('image', click)
cv.waitKey(0)
cv.destroyAllWindows()