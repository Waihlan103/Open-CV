import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg')

layer = img.copy()

for i in range(3):
    layer = cv.pyrDown(layer)
    cv.imshow(str(i), layer)

cv.imshow("ORg", img)
cv.waitKey(0)
cv.destroyAllWindows()