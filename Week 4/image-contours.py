import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('baseball.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Numbers of contours " + str(len(contours)))
print(contours[0])

for contour in contours:
    area = cv.contourArea(contour)
    print(area)

    if area > 500:
        cv.drawContours(img, contour, -1, (0, 255, 0), 3)
        cv.drawContours(imgray, contour, -1, (0, 255, 0), 3)

titles = ['original image', 'gray image']
images = [img, imgray]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles)

plt.show()