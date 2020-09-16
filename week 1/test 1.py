import cv2 as cv
import numpy as np

img = cv.imread("beckham.jpg", 1)

#Accessing pixel value
px = img [50,50]
print(px)

#Accessing blue pixel
blue = img[50,50,0]
print(blue)

#Accessing image properties
print(img.size)
print(img.shape)
print(img.dtype)




