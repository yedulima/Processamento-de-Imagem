import numpy as np
import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread("images/rua.jpg")
imagem = cv2.resize(imagem, (0, 0), fx=2, fy=2)

def imgShow(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    plt.imshow(imagem)
    plt.show()

def setRed(imagem):
    height, width, color = imagem.shape
    for y in range(height):
        for x in range(width):
            imagem.itemset((y, x, 0), 2)
            imagem.itemset((y, x, 1), 2)

    return imagem

imgShow(imagem)
setRed(imagem)
imgShow(imagem)
cv2.imwrite("rua_vermelha.jpg", imagem)