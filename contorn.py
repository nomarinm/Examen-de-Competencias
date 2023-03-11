import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils


imagen1 = cv2.imread('img/patronnn.png')
imagenP = cv2.imread('img/patronREs.jpg')
grises = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
imagen = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
bordes = cv2.Canny(grises, 10, 150)
cv2.imshow('Imagen canny', bordes)
cv2.waitKey(0)
ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
j = 0
mask = np.zeros(np.shape(imagen), np.uint8)  # crea mascara RGB
contornos = []
colores =[(105,191,173),(253,191,0),(0,163,207),(51,51,51),
          (149,146,199),(183,205,0),(219,81,151),(61,61,61),
          (76,114,31),(108,31,121),(255,229,0),(136,134,134),
          (103,130,167),(236,96,129),(230,49,18),(191,192,192),
          (246,172,152),(85,103,174),(15,165,56),(227,227,227),
          (125,80,56),(241,132,0),(0,80,159),(255,255,255)]
clv= colores[0]
print("colores", colores[0],clv)
for i, c in enumerate( ctns):
    area = np.int16(cv2.contourArea(c))
    print(area)
    if area >= 21000:
        j += 1
        cv2.drawContours(imagen, ctns[i], -1, (0,0,255), 2)
        #cv2.drawContours(mask, ctns[i], -1, colores[i], -1)
        contornos.append(ctns[i])
        
        #cv2.imshow('imagen',imagen)
        #cv2.waitKey(0)
print('Número de contornos encontrados: ', len(ctns),j)
print(len(contornos))
#mask = np.zeros(shape=np.shape(imagen)[:2], dtype=np.uint8())  # crea mascara
#i = 1
for i, c in enumerate(contornos):
    print("hola",i)
    cv2.drawContours(mask, [c], -1, colores[i], -1)
    


cv2.imshow('Imagen', imagen)
cv2.imshow('Imagen masksss', mask)
cv2.waitKey(0)
imagD = imutils.resize(mask, height=1600)  # Redimensiona a 720 px
plt.imshow(imagenP)
plt.show()
cv2.imwrite("img/patron.jpg", cv2.cvtColor(imagD, cv2.COLOR_RGB2BGR))  # Guarda la mascara del patron
cv2.destroyAllWindows()