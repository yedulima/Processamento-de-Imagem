import cv2

img = cv2.imread("images/rodovia.jpg")

img = cv2.resize(img, (int(img.shape[1]/6), int(img.shape[0]/6)), interpolation=cv2.INTER_AREA)

#cv2.rectangle(img, (200, 50), (220, 125), (255, 0, 0), -1)
#cv2.putText(img, "Rua", (15, 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)

height, widht, _ = img.shape

center = widht // 2, height // 2

img_centro = img[height: center[1], widht: center[0]]

M = cv2.getRotationMatrix2D(img_centro, 30, 1)
img_centro = cv2.warpAffine(img, M, (widht, height))

while True:
    #cv2.imshow("Rodovia", img)
    cv2.imshow("Rodovia recorte centro", img_centro)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break