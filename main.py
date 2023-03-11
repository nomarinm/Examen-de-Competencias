from plantcv import plantcv as pcv
import matplotlib.pyplot as plt

from puntos import *
import cv2
import numpy as np


if __name__ == '__main__':
    rojo = (0, 0, 255)
    img = cv2.imread('img/pixelperfect.jpg')
    #imageDraw = imutils.resize(img, height=1000)
    imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('patronH.jpg', img)
    print(img.shape[1], img.shape[0])

    color = ('b','g','r')

    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color = c)
        plt.xlim([0,256])

    plt.show()
    plt.imshow(imgBGR)
    plt.show()
    cv2.destroyAllWindows()