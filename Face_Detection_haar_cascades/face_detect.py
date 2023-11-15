import cv2 as cv

img = cv.imread("../Photos/woman.jpg")
# cv.imshow("Woman", img)



grey = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)


haar = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)









cv.waitKey(0)
