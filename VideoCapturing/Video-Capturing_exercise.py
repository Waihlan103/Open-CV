import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('my_video.avi', fourcc, 20.0, (640, 360))
print(cap.isOpened())
while (cap.isOpened()):
    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("My Video Capture", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()