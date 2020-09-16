import cv2 as cv

def nothing(x):
    pass

img = cv.imread('beckham.jpg', 0)

cv.namedWindow('canny')

cv.createTrackbar('lower', 'canny', 0, 255, nothing)
cv.createTrackbar('upper', 'canny', 0, 255, nothing)

while(1):
    lower = cv.getTrackbarPos('lower', 'canny')
    upper = cv.getTrackbarPos('upper', 'canny')
    blurred = cv.GaussianBlur(img, (5, 5), 0)
    edges = cv.Canny(blurred, lower, upper)

    cv.imshow('original', img)
    cv.imshow('canny', edges)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
