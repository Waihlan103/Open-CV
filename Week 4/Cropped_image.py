import cv2
from matplotlib import pyplot as plt

original_img = cv2.imread('coins2.jpg')
imgray = cv2.cvtColor( original_img, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur( imgray, (11,11), 0)
edge_detection = cv2.Canny( blurred_image, 30, 150)

contours, _ = cv2.findContours( edge_detection.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour_image = original_img.copy()
cv2.drawContours(contour_image, contours, -1, (0,255,0), 3)

cropped = []

for (item, count) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(count)

    cropped_coin = original_img[y: y + h, x: x + w]
    cropped.append(cropped_coin)

titles = ['Original_image', 'Blurred Image', 'Canny Image', 'Contoured Image','Cropped Image']
images = [original_img, blurred_image, edge_detection, contour_image, cropped_coin]


for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(original_img[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.figure()

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(cropped[i], 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()
