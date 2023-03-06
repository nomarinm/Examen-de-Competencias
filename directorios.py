from tkinter import filedialog as fd
from pathlib import Path
import sys
import os
from tkinter.messagebox import showinfo
from tkinter import messagebox
from plantcv import plantcv as pcv
from plantcv.plantcv.transform import quick_color_check
from plotnine import *
import numpy as np
import pandas as pd

from puntos import *


def abrir():
    messagebox.showinfo(message="Elija la imágen target", title="Elegir target")
    filenameTarget = fd.askopenfilename(
        filetypes=(
            ("Imagenes", "*.jpg"),
            ("Todos los archivos", "*.*")),
        initialdir="/ven"
    )

    messagebox.showinfo(message="Elija la imágen a corregir", title="Elegir imágen a corregir")
    filenameSource = fd.askopenfilename(
        filetypes=(
            ("Imagenes", "*.jpg"),
            ("Todos los archivos", "*.*")),
        initialdir="/ven"
    )

    rojo = (0, 0, 255)
    target_img, t_path, t_filename = pcv.readimage(filename=filenameTarget)
    target_img = pcv.transform.rotate(target_img, -90, False)
    puntosTarget = tomarPuntos('Imagen para tomar puntos', target_img, rojo)
    maskTarget = BuildMask(puntosTarget, target_img, 1, 50)
    cv2.imwrite("img/maskTarget.jpg", maskTarget)  # Guarda la mascara

    rojo = (0, 0, 255)
    source_img, s_path, s_filename = pcv.readimage(filename=filenameSource)
    source_img = pcv.transform.rotate(source_img, -90, False)
    puntosSource = tomarPuntos('Imagen para tomar puntos', source_img, rojo)
    maskSource = BuildMask(puntosSource, source_img, 1, 50)
    cv2.imwrite("img/maskSource.jpg", maskSource)  # Guarda la mascara

    target_img = cv2.imread("img/target.jpg")
    source_img = cv2.imread("img/source.jpg")
    maskTarget = cv2.imread("img/maskTarget.jpg", -1)  # mask must be read in "as-is" include -1
    maskSource = cv2.imread("img/maskSource.jpg", -1)  # mask must be read in "as-is" include -1
    # .npz files containing target_matrix, source_matrix, and transformation_matrix will be saved to the output_directory file path
    output_directory = "./test1"

    target_matrix, source_matrix, transformation_matrix, corrected_img = pcv.transform.correct_color(target_img,
                                                                                                     maskTarget,
                                                                                                     source_img,
                                                                                                     maskSource,
                                                                                                     output_directory)
    cv2.imwrite("img/corregida.jpg", corrected_img)  # Guarda la correción

    plt.subplot(2, 3, 1)
    plt.title('Source Image')
    plt.imshow(cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB))
    plt.subplot(2, 3, 2)
    plt.title('Corrected Image')
    plt.imshow(cv2.cvtColor(corrected_img, cv2.COLOR_BGR2RGB))
    plt.subplot(2, 3, 3)
    plt.title('Target Image')
    plt.imshow(cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB))
    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([source_img], [i], None, [256], [0, 256])
        plt.subplot(2, 3, 4)
        plt.title('Hist Source Image')
        plt.plot(hist, color = c)
        plt.xlim([0,256])
    for i, c in enumerate(color):
        hist = cv2.calcHist([corrected_img], [i], None, [256], [0, 256])
        plt.subplot(2, 3, 5)
        plt.title('Hist Corrected Image')
        plt.plot(hist, color = c)
        plt.xlim([0,256])
    for i, c in enumerate(color):
        hist = cv2.calcHist([target_img], [i], None, [256], [0, 256])
        plt.subplot(2, 3, 6)
        plt.title('Hist Target Image')
        plt.plot(hist, color = c)
        plt.xlim([0,256])
    plt.show()

    

    quick_color_check(source_matrix=source_matrix, target_matrix=target_matrix, num_chips=24)
def calHistograma(idImage,image,row,col,num):
    color = ('b','g','r')

    for i, c in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        
        plt.imshow(cv2.cvtColor(hist, cv2.COLOR_BGR2RGB))
        plt.plot(hist, color = c)
        plt.xlim([0,256])

