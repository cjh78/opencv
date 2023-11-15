import cv2 as cv


img = cv.imread("Photos/boston.jpg")

cv.imshow("Image", img)

###  converting an Img to GreyScale  ###


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale", gray)


## Blurring an Img ##   |Kernal Size Tuple must be an odd number|

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

cv.imshow("Blurred", blur)


## Edge Cascading ##

canny = cv.Canny(img, 125, 175)
cv.imshow("Edges", canny)


## Dilating An Image ##

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)


# Eroding ##

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)


## Resize  ##  | Cubic takes the longest but is the hightest quality |

resize = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resize)


## Cropping  ## | array slicing |

cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
