import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarites1.jpg', cv.IMREAD_GRAYSCALE)
image = cv.resize(img, (400, 300), interpolation=cv.INTER_AREA)

_, mask = cv.threshold(image, 220, 225, cv.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)

erosion = cv.erode(mask, kernel, iterations=1)

dilation = cv.dilate(mask, kernel, iterations=2)

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)

titles = ['image', 'erosion', 'dilation', 'opening', 'closing', 'gradient']
images = [img, erosion, dilation, opening, closing, gradient]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

