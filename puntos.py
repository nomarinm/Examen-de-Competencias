import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
from plantcv import plantcv as pcv

""" Esta funcion recibe una imagen para tomar puntos en ella"""


def tomarPuntos(idImageStr, image, color):
    ancho = image.shape[1]  # Calcula ancho
    alto = image.shape[0]  # Calcula alto
    if alto > 1000:  # si la imagens es muy grande hace un resize para poder visualizar con opencv
        imageDraw = imutils.resize(image, height=1000)  # Redimensiona a 720 px
        relacion = (alto / imageDraw.shape[0])  # Obtiene la relacion de la imagen original
    else:  # si el tamaño de la imagen es adecuado lo deja igual
        imageDraw = image
        relacion = 1
    puntos = []  # aqui se guardan los puntos
    imageContour = imageDraw.copy()
    def click(event, x, y, flags, param):  # funcion para capturar el click
        if event == cv2.EVENT_LBUTTONDOWN:  # si se pulsa click click isquierdo
            puntos.append([x, y])  # agrega el punto a la lista

    cv2.namedWindow(idImageStr)  # identifica la imagen
    cv2.setMouseCallback(idImageStr, click)  # Callback para trabajar con el click

    while True:
        cv2.imshow(idImageStr, imageDraw)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):  # si se presiona la 'x' termina de tomar puntos
            cv2.destroyWindow(idImageStr)  # una vez selecionados los puntos cierra la imagen
            points1 = puntos.copy()
            #BuildMask(puntos, imageContour, 0, 10)  # dibuja los contornos sobre el patrón
            break

        if len(puntos) > 0:  # si hay puntos los dibuja
            cv2.circle(imageDraw, (puntos[-1][0], puntos[-1][1]), 1, color, -1)
            # se dibuja un rectangulo con centro en el punto seleccionado
            x1 = puntos[-1][0]-5
            y1 = puntos[-1][1]-5
            x2 = puntos[-1][0]+5
            y2 = puntos[-1][1]+5
            cv2.rectangle(imageDraw, (x1, y1), (x2, y2), (255, 0, 0), 2)

    #print("puntos con click ", points1)
    points1 = np.array(points1)
    #print("puntos a escala", np.int16(relacion * points1))
    return np.int16(relacion * points1)  # retorna los puntos a la escala de la imagen original

def BuildMask(puntos, imageDraw, mask, tamanoRoi):
    roi = [tamanoRoi, tamanoRoi]
    chips = []
    X1 = puntos[0][0] - 5
    Y1 = puntos[0][1] - 5
    xx = (puntos[1][0] - 5) - X1
    Y2 = puntos[2][1] - 5
    # declare y_shift
    y_shift = Y2 - Y1
    chips.append(pcv.roi.rectangle(img=imageDraw, x=X1, y=Y1, w=roi[0], h=roi[1]))  # white
    chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + xx, y=Y1, w=roi[0], h=roi[1]))  # blue
    chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + (xx * 2), y=Y1, w=roi[0], h=roi[1]))  # orange
    chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + (xx * 3), y=Y1, w=roi[0], h=roi[1]))  # brown

    # Número de filas de patron
    row_total = 6
    # construye las otras filas
    for i in range(1, row_total):
        chips.append(pcv.roi.rectangle(img=imageDraw, x=X1, y=Y1 + i * (y_shift), w=roi[0], h=roi[1]))
        chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + xx, y=Y1 + i * (y_shift), w=roi[0], h=roi[1]))
        chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + (xx * 2), y=Y1 + i * (y_shift), w=roi[0], h=roi[1]))
        chips.append(pcv.roi.rectangle(img=imageDraw, x=X1 + (xx * 3), y=Y1 + i * (y_shift), w=roi[0], h=roi[1]))

    for chip in chips:
        #print(chip)
        cv2.drawContours(imageDraw, chip[0], -1, (0, 0, 255), 4)

    if mask == 1:  # si se elije construir mascara
        #del chips[0]  # elimina contorno 0 (blanco)
        #del chips[19]  # elimina contorno 19 (negro)
        mask = np.zeros(shape=np.shape(imageDraw)[:2], dtype=np.uint8())  # crea mascara
        i = 1
        for chip in chips:
            #print(chip)
            mask = cv2.drawContours(mask, chip[0], -1, (i * 10), -1)
            i += 1
        #cv2.imwrite("img/mas_mask.jpg", mask)  # Guarda la mascara

    plt.subplot(1, 2, 1)
    plt.title('Target')
    plt.imshow(cv2.cvtColor(imageDraw, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title('Máscara')
    plt.imshow(mask, cmap='gray')
    plt.show()
    return mask
