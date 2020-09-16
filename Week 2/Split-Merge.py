import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', 1)

B, G, R = cv.split(img)
cv.imshow("B", B)
cv.imshow("G", G)
cv.imshow("R", R)

merged = cv.merge((B, G, R))
cv.imshow("Merged", merged)

cv.waitKey(0)
cv.destroyAllWindows()