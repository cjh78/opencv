import cv2 as cv

img = cv.imread("Photos/cat_large.jpg")
cv.imshow('Cat', img)



def rescale_frame(frame, scale=0.75):
    width = frame.shape[1] * scale
    height = frame.shape[0 * scale]

cv.waitKey(0)
