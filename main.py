import cv2 as cv

img = cv.imread('images/rua.jpg')

altura, largura = img.shape[0], img.shape[1]

for y in range(altura):
    for x in range(largura):
        img.itemset((y, x, 0), 2)
        img.itemset((y, x, 1), 2)

cv.imshow('Rua', img)
cv.waitKey(0)