import cv2 as cv
import numpy as np

img = cv.imread("Photos/woman.jpg")
cv.imshow("Normal", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)


grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

# blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

# canny = cv.Canny(img, 125,175)
# cv.imshow("Edges", canny)


## Thresh - changes the pixel colour depending on its intensity whcih we define ##
# 125 threshold value -- 255 maximum value
ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Contours drawn", blank)







cv.waitKey(0)
