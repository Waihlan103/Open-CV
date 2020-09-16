import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('beckham.jpg')

layer = img.copy()

for i in range(3):
    layer = cv.pyrDown(layer)
    cv.imshow(str(i), layer)

cv.imshow('Org', img)
cv.waitKey(0)
cv.destroyAllWindows()
