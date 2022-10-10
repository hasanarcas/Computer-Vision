import cv2 as cv
import numpy as np

img = cv.imread("photos/group 1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("THRESHOLD", thresh)

blank = np.zeros(img.shape, dtype="uint8")

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("CONTOURS", blank)


cv.waitKey(0)