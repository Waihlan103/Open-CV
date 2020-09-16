import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)
cv.namedWindow("Color Tracker")
cv.createTrackbar("LH", "Color Tracker", 0, 255, nothing)
cv.createTrackbar("LS", "Color Tracker", 0, 255, nothing)
cv.createTrackbar("LV", "Color Tracker", 0, 255, nothing)

cv.createTrackbar("UH", "Color Tracker", 0, 255, nothing)
cv.createTrackbar("US", "Color Tracker", 0, 255, nothing)
cv.createTrackbar("UV", "Color Tracker", 0, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    LH = cv.getTrackbarPos("LH", "Color Tracker")
    LS = cv.getTrackbarPos("LS", "Color Tracker")
    LV = cv.getTrackbarPos("LV", "Color Tracker")

    UH = cv.getTrackbarPos("UH", "Color Tracker")
    US = cv.getTrackbarPos("US", "Color Tracker")
    UV = cv.getTrackbarPos("UV", "Color Tracker")

    l_b = np.array([LH, LS, LV])
    u_b = np.array([UH, US, UV])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("mask", mask)
    cv.imshow("result", res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()






