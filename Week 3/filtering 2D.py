import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('water.jpg')
kernal = np.ones((5,5), np.float32)/25
dst = cv.filter2D( img, -1, kernal)

blur = cv.blur( img, (5,5))

Median = cv.medianBlur( img, 5)

titles = ['org','dst','blur','median']
images = [img,dst,blur,Median]

for i in range(4):
    plt.subplot( 2, 2, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()