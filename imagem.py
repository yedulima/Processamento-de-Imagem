import numpy as np
import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread("images/rua.jpg")
print(imagem.shape)
imagem = cv2.resize(imagem, (275, 183))
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def imgShow(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    plt.imshow(imagem)
    plt.show()

def setRed(imagem):
    height, width = imagem.shape[:2]
    for y in range(height):
        for x in range(width):
            imagem.itemset((y, x, 0), 2)
            imagem.itemset((y, x, 1), 2)

    return imagem

ret, mask = cv2.threshold(imagem, 100, 255, cv2.THRESH_BINARY)
plt.imshow(mask)
plt.show()

if __name__ == "__main__":
    print("Ata")

'''
imgShow(imagem)
setRed(imagem)
imgShow(imagem)
cv2.imwrite("rua_vermelha.jpg", imagem)
'''