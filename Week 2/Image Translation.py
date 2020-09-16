import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', 1)

M = np.float32([[1, 0, 25], [0, 1, 67]])

shifted = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv.imshow('Translation', shifted)
cv.waitKey(0)
cv.destroyAllWindows()