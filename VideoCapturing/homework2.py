import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Color Tracker')
cv2.createTrackbar("LH", "Color Tracker", 0, 255, nothing)
cv2.createTrackbar("LS", "Color Tracker", 0, 255, nothing)
cv2.createTrackbar("LV", "Color Tracker", 0, 255, nothing)

cv2.createTrackbar("UH", "Color Tracker", 255, 255, nothing)
cv2.createTrackbar("US", "Color Tracker", 255, 255, nothing)
cv2.createTrackbar("UV","Color Tracker", 255, 255, nothing)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Color Tracker")
    l_s = cv2.getTrackbarPos("LS", "Color Tracker")
    l_v = cv2.getTrackbarPos("LV", "Color Tracker")

    u_h = cv2.getTrackbarPos("UH", "Color Tracker")
    u_s = cv2.getTrackbarPos("US", "Color Tracker")
    u_v = cv2.getTrackbarPos("UV", "Color Tracker")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        print(contour)

        if area > 4000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
