import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('beckham.jpg', 0)
blurred = cv.GaussianBlur(img, (5, 5), 0)

edges = cv.Canny(blurred, 150, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
plt.show()


