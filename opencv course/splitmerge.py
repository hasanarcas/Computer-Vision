import cv2 as cv
import numpy as np

img = cv.imread("photos/group 1.jpg")
cv.imshow("Group", img)

b, g, r = cv.split(img)

# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)

# merged = cv.merge([b, g, r])
# cv.imshow("Merged", merged)


blank = np.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


cv.waitKey(0)