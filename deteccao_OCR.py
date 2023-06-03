from matplotlib import pyplot as plt
import cv2
import numpy as np
import pytesseract
from morfologia_matematica import processamentoImagem

imagem = processamentoImagem("images/placa_carro2.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
text = (pytesseract.image_to_string(imagem, config=custom_config))

def separarLista(text):
    a = text[:-2].split(" ")
    possibilidades = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    placa = ''
    for i in range(len(a)):
        if len(a[i]) > 6:
            for indice in a[i]:
                if indice in possibilidades:
                    placa += indice
    print(placa)

separarLista(text)

plt.imshow(imagem)
plt.show()