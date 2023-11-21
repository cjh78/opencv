import os
import cv2 as cv
import numpy as np

people = ['Madonna', 'Elton John', 'Mindy Kaling',
          'Ben Afflek', 'Jerry Seinfield']

DIR = r'/home/cjh78/code/cjh78/Projects/OpenCV/Face_Recognition_OpenCV/train'

haar = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            grey = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar.detectMultiScale(grey, scaleFactor=1.1,
                                              minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = grey[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training Complete ✔️")
# print(f"Length of features = {len(features)}")
# print(f"Length of labels = {len(labels)}")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

## Training the Face Recognizer ##

face_recognizer.train(features, labels)

# Allows us to use the trained model in another file
# without the need for all o fthe trailing code #

face_recognizer.save('faces_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)
