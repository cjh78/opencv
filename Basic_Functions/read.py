import cv2 as cv

#### READING IMAGE FILE ####

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('cat', img)

# cv.waitKey(0)

#### READING VIDEO FILE ####

# ||- can use either filepath for video -||
# ||- or 0,1,2 for webcam=0/external cameras in order of 1 -> -||

capture = cv.VideoCapture('Videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
