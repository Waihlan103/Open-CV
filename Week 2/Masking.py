import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', 1)
cv.imshow("ORG", img)

mask = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1]//2, img.shape[0]//2)

cv.rectangle(mask, (cX - 60, cY - 60), (cX + 60, cY + 60), 255, -1)
cv.imshow('mask', mask)

masking = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masking", masking)
cv.waitKey(0)
cv.destroyAllWindows()