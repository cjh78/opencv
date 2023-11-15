import cv2 as cv
import numpy as np



img = cv.imread("Photos/boston.jpg")
cv.imshow("Normal", img)


### Splitting into colour components eg R-G-B ###


b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# Dsiplays in Greyscale #
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

##  Merge ##
# Order matters #
merged = cv.merge([b,g,r,])
cv.imshow('Merged', merged)







cv.waitKey(0)
