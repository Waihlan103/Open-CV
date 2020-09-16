import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudokul.jpg', cv.IMREAD_GRAYSCALE)

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_Combined = cv.bitwise_and(sobelX, sobelY)

titles = ['image', 'sobelX', 'sobelY', 'sobel_Combined']

images = [img, sobelX, sobelY, sobel_Combined]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles)

plt.show()