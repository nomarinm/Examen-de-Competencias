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
from graficar import *


def nuevaFoto():
    target_img = cv2.imread("img/camara1/patron.jpg")    
    target_mask = cv2.imread("img/camara1/maskPatron.jpg", -1) # mask must be read in "as-is" include -1

    messagebox.showinfo(message="Elija la imágen de referencia", title="Elegir imágen a corregir")
    filenameSource = fd.askopenfilename(
        filetypes=(
            ("Imagenes", "*.jpg"),
            ("Todos los archivos", "*.*")),
        initialdir="/ven"
    )
    rojo = (0, 0, 255)
    source = cv2.imread(filenameSource)
    plt.title('source Image')
    plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
    plt.show()
    puntosSource = tomarPuntos('Imagen para tomar puntos', source.copy(), rojo)
    maskSource = BuildMask(puntosSource, source, 1, 50)
    cv2.imwrite("./img/camara1/maskSource.jpg", maskSource)  # Guarda la mascara
    target_img = cv2.imread("img/camara1/patron.jpg")    
    target_mask = cv2.imread("img/camara1/maskPatron.jpg", -1) # mask must be read in "as-is" include -1
    source = cv2.imread(filenameSource)
    maskSource = cv2.imread("./img/camara1/maskSource.jpg", -1)  # mask must be read in "as-is" include -1
    
    """
    # get color matrix of target and save
    target_headers, target_matrix = pcv.transform.get_color_matrix(target_img, target_mask)
    pcv.transform.save_matrix(target_matrix, "img/camara1/target.npz")

    #get color_matrix of source
    source_headers, source_matrix = pcv.transform.get_color_matrix(source, maskSource1)
    matrix_a, matrix_m, matrix_b = pcv.transform.get_matrix_m(target_matrix= target_matrix, 
                                                              source_matrix= source_matrix)
    source = cv2.imread(filenameSource)
    
    plt.title('Target Image')
    plt.imshow(cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB))
    plt.show()
    deviance, transformation_matrix1 = pcv.transform.calc_transformation_matrix(matrix_m, matrix_b)
    
    corrected_img = pcv.transform.apply_transformation_matrix(source_img= source, 
                                                              target_img= target_img, 
                                                              transformation_matrix= transformation_matrix1)
    
    pcv.transform.save_matrix(transformation_matrix1, "./img/camara1/test1/matrix1.npz")
    plt.title('Source Image')
    plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.title('Corrected Image')
    plt.imshow(cv2.cvtColor(corrected_img, cv2.COLOR_BGR2RGB))
    plt.show()
    
    

    print("aqui llega")
    
    """
    

    output_directory = "./img/camara1/test1"
    #maskSource = cv2.imread("img/camara1/maskSource.jpg", -1)  # mask must be read in "as-is" include -1

    target_matrix, source_matrix, transformation_matrix, corrected_img = pcv.transform.correct_color(target_img,
                                                                                                     target_mask, 
                                                                                                     source, 
                                                                                                     maskSource, 
                                                                                                     output_directory)
    
    plt.subplot(1, 2, 1)
    plt.title('Imagen de referencia')
    plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title('Corrected Image')
    plt.imshow(corrected_img)
    plt.show()
    
    

    

    messagebox.showinfo(message="Elija la imágen a corregir", title="Elegir imágen a corregir")
    filenameSource1 = fd.askopenfilename(
        filetypes=(
            ("Imagenes", "*.jpg"),
            ("Todos los archivos", "*.*")),
        initialdir="/ven"
    )

    new_source1 = cv2.imread(filenameSource1) #read in new image for transformation
    target_img = cv2.imread("img/camara1/patron.jpg")    
    plt.title('source Image')
    plt.imshow(cv2.cvtColor(new_source1, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.title('target Image')
    plt.imshow(cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB))
    plt.show()
    Transformation_matrix = pcv.transform.load_matrix("./img/camara1/test1/matrix1.npz") #load in transformation_matrix
    cor_img = pcv.transform.apply_transformation_matrix(source_img=new_source1, 
                                                        target_img=target_img, 
                                                        transformation_matrix=transformation_matrix) #apply transformation
    
    
    plt.subplot(1, 2, 1)
    plt.title('Source Image')
    plt.imshow(cv2.cvtColor(new_source1, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title('Corrected Image')
    plt.imshow(cv2.cvtColor(cor_img, cv2.COLOR_BGR2RGB))
    plt.show()

    #  defino lista con imagenes de fuente y corregida
    #listaimg =[new_source1, corrected_img]
    #hist = calHistograma(listaimg)
    #graficarHist(hist)
    #graficaBrillo(listaimg)



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
    #target_img, t_path, t_filename = pcv.readimage(filename=filenameTarget)
    target_img = cv2.imread(filenameTarget)
    """
    plt.imshow(target_img)
    plt.show()"""
    #target_img = pcv.transform.rotate(target_img, -90, False)
    puntosTarget = tomarPuntos('Imagen para tomar puntos', target_img, rojo)
    maskTarget = BuildMask(puntosTarget, target_img, 1, 20)
    cv2.imwrite("img/maskTarget.jpg", maskTarget)  # Guarda la mascara

    rojo = (0, 0, 255)
    #source_img, s_path, s_filename = pcv.readimage(filename=filenameSource)
    source_img = cv2.imread(filenameSource)
    #plt.imshow(source_img)
    #plt.show()
    #source_img = pcv.transform.rotate(source_img, -90, False)
    puntosSource = tomarPuntos('Imagen para tomar puntos', source_img, rojo)
    maskSource = BuildMask(puntosSource, source_img, 1, 20)
    cv2.imwrite("img/maskSource.jpg", maskSource)  # Guarda la mascara

    target_img = cv2.imread(filenameTarget)
    source_img = cv2.imread(filenameSource)
    print("aqui llega")
    maskTarget = cv2.imread("img/maskTarget.jpg", -1)  # mask must be read in "as-is" include -1
    maskSource = cv2.imread("img/maskSource.jpg", -1)  # mask must be read in "as-is" include -1
    print("aqui llega1")
    # .npz files containing target_matrix, source_matrix, and transformation_matrix will be saved to the output_directory file path
    output_directory = "./test1"

    target_matrix, source_matrix, transformation_matrix, corrected_img = pcv.transform.correct_color(target_img,
                                                                                                     maskTarget,
                                                                                                     source_img,
                                                                                                     maskSource,
                                                                                                     output_directory)
    cv2.imwrite("img/corregida.jpg", corrected_img)  # Guarda la correción
    listImg = [source_img, corrected_img, target_img]
    graficar(listImg)
    #histo = calHistograma(listImg)
    #graficarHist(histo)
    #HistBrillo = graficaBrillo(listImg)

    transformation_matrix = pcv.transform.load_matrix("test1/transformation_matrix.npz") #load in transformation_matrix
    #transformation_matrix = pcv.transform.load_matrix("test1/trans_patron_matrix.npz")

    #new_source = cv2.imread("img/camara1/C3I.jpg") #read in new image for transformation
    messagebox.showinfo(message="Elija la imágen a corregir", title="Elegir imágen a corregir")
    filenameSource = fd.askopenfilename(
        filetypes=(
            ("Imagenes", "*.jpg"),
            ("Todos los archivos", "*.*")),
        initialdir="/ven"
    )
    new_source = cv2.imread(filenameSource)
    co_img = pcv.transform.apply_transformation_matrix(source_img= new_source, target_img= target_img, transformation_matrix= transformation_matrix) #apply transformation
    cv2.imwrite("img/corregida_prueba.jpg", co_img)  # Guarda la correción
    print("nueva correcion")
    plt.imshow(cv2.cvtColor(co_img, cv2.COLOR_BGR2RGB))
    plt.title("imagen corregida")
    plt.show()