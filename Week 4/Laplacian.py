import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

cv.imshow("org", img)
cv.imshow("edge", lap)
cv.waitKey(0)
cv.destroyAllWindows()