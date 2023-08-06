import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 4), np.uint8)

y, x = img.shape[:2]

# Quadrado
cv.rectangle(img, (0, 0), (x, y), (0, 175, 0), -1)

# Triangulos
t1 = np.array([(x // 2, y // 4), (x // 6, y // 2), (x // 2, y // 2)])
t2 = np.array([(x // 6, y // 2), (x // 2, 384), (x // 2, y // 2)])
t3 = np.array([(x // 2, 384), (432, y // 2), (x // 2, y // 2)])
t4 = np.array([(432, y // 2), (x // 2, y // 4), (x // 2, y // 2)])

cv.drawContours(img, [t1], 0, (0, 255, 255), -1)
cv.drawContours(img, [t2], 0, (0, 255, 255), -1)
cv.drawContours(img, [t3], 0, (0, 255, 255), -1)
cv.drawContours(img, [t4], 0, (0, 255, 255), -1)

# Circulo
cv.circle(img, (x // 2, y // 2), 50, (255, 0, 0), -1)

cv.imshow('Bandeira do Brasil', img)
cv.waitKey(0)