import cv2 as cv
import numpy as np

img = cv.imread('sudokul.jpg', 0)
#th2 = cv.adaptiveThreshold( img, 225, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 3)

th2 = cv.adaptiveThreshold( img, 225, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 3)

cv.imshow("image", img)
cv.imshow("thresold", th2)
cv.waitKey(0)
cv.destroyAllWindows()