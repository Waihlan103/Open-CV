import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('invisible_man.avi', fourcc, 20.0, (640, 480))
time.sleep(2)
background = 0
for i in range(30):
    ret, background = cap.read()

while cap.isOpened():
    ret, img = cap.read()

    if not ret:
        break

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv.morphologyEx(mask1, cv.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask2 = cv.morphologyEx(mask1, cv.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv.bitwise_not(mask1)

    res1 = cv.bitwise_and(background, background, mask=mask1)
    res2 = cv.bitwise_and(img, img, mask=mask2)

    final_output = cv.addWeighted(res1, 1, res2, 1, 0)
    out.write(final_output)

    cv.imshow('invisible_man', final_output)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()