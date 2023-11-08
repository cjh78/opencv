import cv2 as cv

img = cv.imread("Photos/cats-group.jpg")
cv.imshow("Normal", img)

## Averaging ##

average = cv.blur(img, (7,7))
cv.imshow("AVG Blur", average)


gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)


## Median Blur ##
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

## Bilateral Blur ##
# | Applies blur while maintaining edges | #
# Most Effecive #

# Similar to Median -- Seems to apply a smudge #
bi_blur = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bi Lateral Filtering", bi_blur)










cv.waitKey(0)
