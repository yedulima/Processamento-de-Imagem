import cv2
from matplotlib import pyplot as plt
import numpy as np

def processamentoImagem(imagem):
    image = cv2.imread(imagem, 0)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    kernel = np.ones((700, 700), np.uint8)

    placa = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    _, image_threshold = cv2.threshold(placa, 127, 255, cv2.THRESH_BINARY_INV)

    return image_threshold

if __name__ == "__main__":
    image = processamentoImagem("images/placa_carro2.jpg")

    plt.imshow(image)
    plt.show()