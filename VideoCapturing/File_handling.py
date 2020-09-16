import cv2 as cv

img = cv.imread("C:/Users/Wai Hlan Kaung/Pictures/Screenshots/Screenshot (14).png")

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()