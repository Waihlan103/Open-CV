import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg')

#cropped = img[25:50, 50:120]

#cv.imshow("crop", cropped)

vertical = cv.flip(img, 0)
horizontal = cv.flip(img, 1)
vertical_horizontal = cv.flip(img, -1)

cv.imshow("Vertical", vertical)
cv.imshow("horizontal", horizontal)
cv.imshow("vertical_horizontal", vertical_horizontal)

cv.waitKey(0)
cv.destroyAllWindows()