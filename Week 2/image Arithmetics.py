import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', 1)
img = cv.resize( img, (200, 160), interpolation=cv.INTER_AREA)

#Adding pixel values
M = np.ones(img.shape, dtype="uint8")*100
adding = cv.add(img, M)
cv.imshow("Adding", adding)

#Subtruct pixel values
N = np.ones(img.shape, dtype="uint8")*100
subtruct = cv.subtract(img, N)
cv.imshow("Subtract", subtruct)
cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()