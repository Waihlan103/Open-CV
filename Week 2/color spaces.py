import cv2 as cv
import numpy as np

img= cv.imread('beckham.jpg', 1)

grey = cv.cvtColor( img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor( img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

cv.waitKey(0)
cv.destroyAllWindows()