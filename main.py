import cv2 as cv

img = cv.imread('images/rua.jpg', 0)

ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

cv.imshow('Rua', thresh)
cv.waitKey(0)