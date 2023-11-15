import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
cv.imshow("This is a cat I think", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


### Simple Thresholding ###

threshold, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)


threshold, thresh_inv = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inversed", thresh_inv)


### Adaotive Thresholding ###


adaptive_thresh = cv.adaptiveThreshold(grey, 255,
                                      cv.ADAPTIVE_THRESH_MEAN_C,
                                      cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Threshold", adaptive_thresh)











cv.waitKey(0)
