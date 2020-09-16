import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

fgbg = cv.createBackgroundSubtractorMOG2(50, 200, True)
frameCount = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frameCount += 1
    resizedframe = cv.resize(frame, (0, 0), fx=0.50, fy=0.50)

    fgmask = fgbg.apply(resizedframe)

    count = np.count_nonzero(fgmask)
    print('Frame: %d, Pixel Count %d' % (frameCount, count))

    if frameCount > 1 and count > 1000:
        print('Moving')
        cv.putText(frame, "Moving", (20, 20), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3, cv.LINE_AA)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", fgmask)

    key = cv.waitKey(5) & 0xFF
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()