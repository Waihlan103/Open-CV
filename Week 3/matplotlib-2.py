import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.jpg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

titles = ["Binary", "Binary_inv", "To_Zero", "To_Zero_Inv", "Turn_C"]
images = [th1, th2, th3, th4, th5]

for i in range(5):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
