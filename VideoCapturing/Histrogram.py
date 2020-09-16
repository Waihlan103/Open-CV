import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img = np.zeros((200, 200), np.uint8)

#cv.rectangle(img, (0,100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
img = cv.imread('C:/Users/Wai Hlan Kaung/PycharmProjects/Open CV/Week 2/beckham.jpg')
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

b, g, r = cv.split(img)

#cv.imshow("b", b)
#cv.imshow("g", g)
#cv.imshow("r", r)
#cv.imshow("picture", img)
plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()