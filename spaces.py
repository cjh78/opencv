import cv2 as cv



img = cv.imread("Photos/boston.jpg")

cv.imshow("Boston", img)

# grey = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)
# cv.imshow("Grey", grey)


# ## BGR to HSV (Hue Saturation Vision) ##

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# ### BGR TO L A B ###

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("L-A-B ", lab)





cv.waitKey(0)
