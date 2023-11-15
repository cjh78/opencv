import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread("Photos/cat.jpg")
cv.imshow("Normal", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grey", grey)

mask =  cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mask", masked)

## Greyscale Histogram ##

# grey_hist = cv.calcHist([grey], [0], mask, [256], [0,256])

# plt.figure()
# plt.title("Greyscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()



## Colour Histogram ##

plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()




cv.waitKey(0)
