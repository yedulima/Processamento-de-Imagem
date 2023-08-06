import cv2
import numpy as np

def processamentoImagem(imagem):
    image = cv2.imread(imagem, 0)

    y, x = image.shape[0], image.shape[1]

    image = cv2.resize(image, (x // 4, y // 4))

    kernel = np.ones((700, 700), np.uint8)

    placa = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    _, image_threshold = cv2.threshold(placa, 127, 255, cv2.THRESH_BINARY_INV)

    return image_threshold

if __name__ == "__main__":
    image = processamentoImagem("images/placa_carro2.jpg")

    cv2.imshow('Placa', image)
    cv2.waitKey(0)