import cv2 as cv

img = cv.imread('beckham.jpg')

first_layer = cv.pyrDown(img)
expended_image = cv.pyrUp(first_layer)
laplacian = cv.subtract(img, expended_image)

cv.imshow('first layer', first_layer)
cv.imshow('expended layer', expended_image)
cv.imshow('laplacian', laplacian)

cv.waitKey(0)
cv.destroyAllWindows()
