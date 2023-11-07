import cv2 as cv
import numpy as np

img = cv.imread("Photos/boston.jpg")

cv.imshow("Boston", img)


## Traslation ## | Moves an image left, right, up, or down |


def translate(img, x, y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, trans_mat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

## Rotation ##

def rotate(img, angle, rot_point=None):
    (height,width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2,height//2)

        rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
        dimensions = (width,height)

        return cv.warpAffine(img, rot_mat, dimensions)

# 45 = anticlockwise
# -45 = clockwise

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)


## Flip ##

# 0 vertically
# 1 horizontally
# -1 is both

flip = cv.flip(img, 0)
cv.imshow("Flipped", flip)




cv.waitKey(0)
