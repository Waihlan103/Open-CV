import cv2 as cv
import numpy as np

img=cv.imread('beckham.jpg')

(h, w) = img.shape[:2]
center = (w//2, h//2)

M = cv.getRotationMatrix2D(center, 270, 1)
rotate = cv.warpAffine(img, M, (w, h))

cv.imshow("image", rotate)
cv.waitKey(0)
cv.destroyWindow()