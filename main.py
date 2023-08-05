import cv2 as cv
import numpy as np

img = cv.imread('images/rua.jpg')

M = np.float32([
	[1, 0, 0.5],
	[0, 1, 1.0]
])

img = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv.imshow("rua", img)
cv.waitKey(0)