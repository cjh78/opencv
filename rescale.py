import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")
# cv.imshow('Cat Large', img)


###RESCALE FUNCITON###

def rescale_frame(frame, scale=0.2):
    #Images | Videos | Live Videos#

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resized_image = rescale_frame(img)
# cv.imshow('Cat Resized', resized_image)

capture = cv.VideoCapture('Videos/video.mp4')

### RESIZE IMAGE FUNC ###

def changeRes(width, height):
    # Live Video Only #

    capture.set(3, width)
    capture.set(4, height)




###READING VIDEOS###

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
