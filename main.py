import cv2 as cv

img = cv.imread('images/rua.jpg', )

#img = cv.Sobel(img, cv.CV_8U, 1, 0)
imgBlur = cv.GaussianBlur(img, (3, 3), 0)

cv.imshow('Rua', img)
cv.imshow('Rua Blur', imgBlur)
cv.waitKey(0)