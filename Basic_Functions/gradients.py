import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats-group.jpg")
cv.imshow("Normal", img)


grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

### Edge detecting ###

## Laplacian ##

lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)



## Sobel ##

sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", sobel_combined)



canny = cv.Canny(grey, 150, 175)
cv.imshow("Canny", canny)






cv.waitKey(0)
