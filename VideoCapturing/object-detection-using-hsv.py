import cv2 as cv
import numpy as np

while True:
    img = cv.imread('smarites1.jpg')
    image = cv.resize(img, (480, 360), interpolation=cv.INTER_AREA)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])
    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(image, image, mask=mask)

    cv.imshow("image", image)
    cv.imshow("mask", mask)
    cv.imshow("result", res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()