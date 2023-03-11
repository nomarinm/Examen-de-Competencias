import matplotlib.pyplot as plt
import cv2


def graficar(listImages):
    imgSource = cv2.cvtColor(listImages[0], cv2.COLOR_BGR2RGB)
    imgCorrected = cv2.cvtColor(listImages[1], cv2.COLOR_BGR2RGB)
    #imgTarget = cv2.cvtColor(listImages[2], cv2.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.title('Source Image')
    plt.imshow(imgSource)
    plt.subplot(1, 2, 2)
    plt.title('Corrected Image')
    plt.imshow(imgCorrected)
    #plt.subplot(1, 3, 3)
    #plt.title('Target Image')
    #plt.imshow(imgTarget)
    plt.suptitle("Corrección de color")
    plt.show()


def calHistograma(listImage): # recibe las imagenes en BGR
    listHisto = []
    for img in listImage:
        histR = cv2.calcHist([img], [2], None, [256], [0, 256])  # canal R
        histG = cv2.calcHist([img], [1], None, [256], [0, 256])  # canal G
        histB = cv2.calcHist([img], [0], None, [256], [0, 256])  # canal B
        listHisto.append([histR, histG, histB])

    return listHisto  # Retorna Lista con los histogramas(R, G, B) de cada imágen

def graficarHist(histogramas):  # recibe los Histogramas de 3 Imágenes

    # muestra los histogramas de las tres imagenes  separados por bandas
    font= 10
    ax1 = plt.subplot(1, 3, 1)
    plt.title('canal R',fontsize= font)
    plt.plot(histogramas[0][0], color = 'c', label="source")  # canal R 1ra Imágen
    plt.plot(histogramas[1][0], color = 'pink', label= "corrected")  # canal R 2da Imágen
    #plt.plot(histogramas[2][0], color = 'r', label= "target")  # canal R 3ra Imágen
    plt.xlabel("Intensidad")
    plt.ylabel("Núnmero de pixeles")
    plt.legend()
    plt.xlim([0,256])

    ax2 = plt.subplot(1, 3, 2, sharey=ax1)
    plt.setp(ax2.get_yticklabels(), visible=False)
    plt.title('canal G',fontsize= font)
    plt.plot(histogramas[0][1], color = 'c',label="source")  # canal G 1ra Imágen
    plt.plot(histogramas[1][1], color = 'pink',label="corrected")  # canal G 2da Imágen
    #plt.plot(histogramas[2][1], color = 'g',label="target")  # canal G 3ra Imágen
    plt.xlabel("Intensidad")
    #  plt.ylabel("Núnmero de pixeles")
    plt.legend()
    plt.xlim([0,256])

    ax3 = plt.subplot(1, 3, 3,sharey=ax1)
    plt.setp(ax3.get_yticklabels(), visible=False)
    plt.title('canal B', fontsize= font)
    plt.plot(histogramas[0][2], color = 'c',label="source")  # canal B 1ra Imágen
    plt.plot(histogramas[1][2], color = 'pink',label="corrected")  # canal B 2da Imágen
    #plt.plot(histogramas[2][1], color = 'b',label="target")  # canal B 3ra Imágen
    plt.xlabel("Intensidad")
    #  plt.ylabel("Núnmero de pixeles")
    plt.legend()
    plt.xlim([0,256])
    plt.suptitle("Histogramas por bandas de color")
    plt.show()

def graficaBrillo(listImages):  # muestra el histograma del brillo para las 3 imágenes
    font = 10
    #  Convierte las 3 imagenes a HSV
    imgSource = cv2.cvtColor(listImages[0], cv2.COLOR_BGR2HSV)
    imgCorrected = cv2.cvtColor(listImages[1], cv2.COLOR_BGR2HSV)
    #imgTarget = cv2.cvtColor(listImages[2], cv2.COLOR_BGR2HSV)

    #  Calcula los 3 Histogramas de las imágenes  del canal V (2)
    histSource = cv2.calcHist([imgSource], [2], None, [256], [0, 256])
    histCorrected = cv2.calcHist([imgCorrected], [2], None, [256], [0, 256])
    #histTarget = cv2.calcHist([imgTarget], [2], None, [256], [0, 256])

    # muestra los Histogramas
    plt.subplot(1, 1, 1)
    plt.title('Canal V (HSV)', fontsize= font)
    plt.plot(histSource, color = 'c',label="source")
    plt.plot(histCorrected, color = 'pink',label="corrected")
    #plt.plot(histTarget, color = 'b',label="target")
    plt.legend()
    plt.xlabel("Intensidad")
    plt.ylabel("Núnmero de pixeles")
    plt.xlim([0,256])
    plt.suptitle("Histograma - brillo de las imágenes")
    #plt.tight_layout()    
    plt.show()

    return [histSource, histCorrected]




    