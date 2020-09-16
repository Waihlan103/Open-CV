import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
background = 0

while cap.isOpened():
    CamWorking, frame = cap.read()

    if CamWorking:
        #hue(color) Saturation(white + color) Value(black + color); hsv - can seen by eyes (color + intensity)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #how we convert rgb to hsv?
        cv.imshow("hsv", hsv) #testing hsv looks

        #how to get hsv value?
        #lower: hue - 10, 100, 100, higher: h+10, 255, 255
        red = np.uint8([[[0, 0, 255]]]) #bgr value of red
        hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV) #get hsv value of red from bgr

        #range of colours hsv value in orange range
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv.inRange(hsv, l_red, u_red)
        cv.imshow("mask", mask)

        #all things orange
        part1 = cv.bitwise_and(background, background, mask=mask)
        cv.imshow("part1", part1)

        mask = cv.bitwise_not(mask)

        #part2 is all things not red
        part2 = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("mask2", part2)

        cv.imshow("cloak", part1 + part2)

        if cv.waitKey(5) == ord('q'):
            break

cap.release()
cv.destroyAllWindows()

