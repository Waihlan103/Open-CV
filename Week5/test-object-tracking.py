import cv2 as cv

cap = cv.VideoCapture('vid2.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blurred, 20, 255, cv.THRESH_BINARY)

    dilate = cv.dilate(thresh, None, iterations=3)

    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 1800:
            continue

        area = cv.contourArea(contour)
        print(area)

        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.putText(frame1, "status : {} ".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv.imshow("frame1", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cap.release()
















