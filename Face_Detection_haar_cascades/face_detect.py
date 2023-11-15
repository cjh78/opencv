import cv2 as cv


img = cv.imread("../Photos/group_1.jpg")
# cv.imshow("Woman", img)


def rescale_frame(frame, scale=0.2):
    #Images | Videos | Live Videos#

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

rescaled_img = rescale_frame(img, 0.2)


grey = cv.cvtColor(rescaled_img, cv.COLOR_BGR2GRAY)


haar = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found = {len(faces_rect)}")


for (x,y,w,h) in faces_rect:
    cv.rectangle(rescaled_img, (x,y), (x+w, y+h), (0.255,0), thickness=2)

cv.imshow("Detected faces", rescaled_img)




cv.waitKey(0)
