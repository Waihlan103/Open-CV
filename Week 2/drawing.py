import cv2 as cv
import numpy as np

img = cv.imread('beckham.jpg', 1)
img = cv.resize( img, (200, 160), interpolation=cv.INTER_AREA)

#cv.line( img, (20, 20), (50, 0), (0, 255, 255), 3)
#cv.arrowedLine( img, (50, 0), (50, 50), (255, 255, 0), 3)

#cv.rectangle( img, (80, 10), (120, 60), (0, 255, 0), 3)

#cv.circle( img, (100, 25), 20, (0, 255, 0), 3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText( img, "Beckham", (10, 150), font, 1, (0, 0, 255), 2)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
