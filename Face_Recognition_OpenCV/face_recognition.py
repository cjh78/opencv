import cv2 as cv
import numpy as np

haar = cv.CascadeClassifier("haar_face.xml")


people = ['Madonna', 'Elton John', 'Mindy Kaling',
          'Ben Afflek', 'Jerry Seinfield']

## if you need to resue these and load the arrays, set >> allow_pickle=True << ##

# features = np.load("features.npy")
# labels = np.load("labels.npy")


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("faces_trained.yml")


img = cv.imread(r'/home/cjh78/code/cjh78/Projects/OpenCV/Photos/group_2.jpg')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow("Person", grey)

## Detecting the facess ##

faces_rect = haar.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = grey[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]),
               (20,20), cv.FONT_HERSHEY_COMPLEX,
               1.0, (0,255,0), 2)

    cv.rectangle(img, (x,y), (x+w, y+h),
                 (0,255,0), thickness=2)


cv.imshow("Detected face", img)




cv.waitKey(0)
