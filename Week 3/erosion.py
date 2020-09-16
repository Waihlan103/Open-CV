import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.jpg', cv.IMREAD_GRAYSCALE)

_, mask = cv.threshold(img, 220, 250, cv.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)
erosion = cv.erode(mask, kernal, iterations=1)

titles = ["Original_image", "Mask", "Erosion"]
images = [ img, mask, erosion]


for i in range(3):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
