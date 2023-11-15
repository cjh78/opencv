import cv2 as cv
import numpy as np


blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow("Blank", blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow("Cat", img)


### Painting the image ###

# blank[200:300, 200:400] = 173,10,155
# cv.imshow("Magenta", blank)

### Rectangle ###

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow("Rectangle", blank)



### Text ###
cv.putText(blank, "I think ", (225,225),
           cv.FONT_HERSHEY_TRIPLEX,
           1.0, (168,39,152), 2)

cv.imshow("Text", blank)



cv.waitKey(0)
