import cv2 as cv

import numpy as np

blank = np.zeros((400,400), dtype="uint8")


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("Circle", circle)


## Bitwaise AND ##
# takes the intersection of the two images and displays them #

bitwise_and = cv.bitwise_and(rectangle, circle)

cv.imshow("Bitwise AND", bitwise_and)


## Bitwise OR ##
# puts the iamges over each other and superimposes the unique regions on them #
bitwise_or = cv.bitwise_or(rectangle, circle)

cv.imshow("Bitwise OR", bitwise_or)


## Bitwise XOR ##
# retruns the non intersecting regions #

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imhsow("Bitwise XOR", bitwise_xor)

## Bitwise NOT ##


bitwise_not_rectangle = cv.bitwise_not(rectangle)
cv.imshow("Rectangle NOT", bitwise_not_rectangle)

bitwise_not_c = cv.bitwise_not(circle)
cv.imshow("Circle NOT", bitwise_not_c)


cv.waitKey(0)
