import cv2 as cv
import numpy as np

img = cv.imread('gradient.jpg', 0)

_, th1 = cv.threshold( img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold( img, 127, 255, cv.THRESH_BINARY_INV)

_, th3 = cv.threshold( img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold( img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold( img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow("Binary", th1)
cv.imshow("Binary_Inv", th2)
cv.imshow("TruN_C", th3)
cv.imshow("To_Zero", th4)
cv.imshow("To_Zero_INV", th5)
cv.waitKey(0)
cv.destroyAllWindows()