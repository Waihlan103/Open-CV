import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('coins2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred_image = cv.GaussianBlur(gray, (11, 11), 0)
edge_detection = cv.Canny(blurred_image, 30, 150)

contours, _ = cv.findContours(edge_detection.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

contour_image = cv.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)

titles = ['Original_image', 'Blurred Image', 'Canny Image', 'Contoured Image']
images = [img, blurred_image, edge_detection, contour_image]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()