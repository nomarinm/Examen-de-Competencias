from plantcv import plantcv as pcv
import matplotlib.pyplot as plt
from puntos import *
import cv2
import numpy as np

import tkinter
from tkinter import ttk
import directorios

root = tkinter.Tk()  # Crea ventana principal
root.title("Color Correction")  # Titulo de la ventana
root.resizable(width=False, height=False)  # no deja redimensionar
root.geometry("300x300")  # redimensiona
# Panel para pestañas
panel = ttk.Notebook(root)
panel.pack(fill='both', expand='yes')
# Crea pestañas
pest1 = ttk.Frame(panel)
pest2 = ttk.Frame(panel)
# Agrega pestañas
panel.add(pest1, text='  CONFIGURAR  ')
panel.add(pest2, text='  LEER DOCUMENTOS  ')

btnDir = ttk.Button(pest1, text='SELECCIONE IMÁGENES', command=directorios.abrir)
btnDir.pack(padx=20, pady=70)
btnDi1 = ttk.Button(pest2, text='SELECCIONE UN DIRECTORIO', command=directorios.abrir)
btnDi1.pack(padx=20, pady=70)

root.mainloop()