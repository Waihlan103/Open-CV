import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while(cap.isOpened()):

    ret, frame = cap.read()

    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("My Video Capture", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()