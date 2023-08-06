import cv2

imagem = cv2.imread("images/rua.jpg")

def setRed(imagem):
    height, width = imagem.shape[:2]
    for y in range(height):
        for x in range(width):
            imagem.itemset((y, x, 0), 2)
            imagem.itemset((y, x, 1), 2)

    return imagem

if __name__ == "__main__":
    cv2.imshow('rua', setRed(imagem))
    cv2.waitKey(0)