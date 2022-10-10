import cv2 as cv

img = cv.imread("photos/park.jpg")
cv.imshow("Group", img)

# averaging
average = cv.blur(img, (5, 5))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("Gaussian Blur", gauss)

# median blur
median = cv.medianBlur(img, 5)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)