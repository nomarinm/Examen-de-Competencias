from plantcv import plantcv as pcv
import matplotlib.pyplot as plt

from puntos import *
import cv2
import numpy as np


if __name__ == '__main__':
    rojo = (0, 0, 255)
    target_img, t_path, t_filename = pcv.readimage(filename="img/source.jpg")
    target_img = pcv.transform.rotate(target_img, -90, False)
    source_img, s_path, s_filename = pcv.readimage(filename="./img/I2.jpg")
    #pcv.plot_image(target_img)
    puntos = tomarPuntos('Imagen para tomar puntos', target_img, rojo)

    BuildMask(puntos, target_img, 1, 50)
    #pcv.plot_image(target_img)

    # dimensions = [50, 50]  # pixel ROI dimensions
    #
    # chips = []
    # # Declare first row:
    # # Inputs:
    # #   img - RGB or grayscale image to plot the ROI on
    # #   x - The x-coordinate of the upper left corner of the rectangle
    # #   y - The y-coordinate of the upper left corner of the rectangle
    # #   h - The height of the rectangle
    # #   w - The width of the rectangle
    # img = target_img.copy()
    # #pcv.plot_image(img)
    # chips.append(pcv.roi.rectangle(img=img, x=940, y=1400, w=dimensions[0], h=dimensions[1]))  # white
    # chips.append(pcv.roi.rectangle(img=img, x=1080, y=1400, w=dimensions[0], h=dimensions[1]))  # blue
    # chips.append(pcv.roi.rectangle(img=img, x=1230, y=1400, w=dimensions[0], h=dimensions[1]))  # orange
    # chips.append(pcv.roi.rectangle(img=img, x=1390, y=1400, w=dimensions[0], h=dimensions[1]))  # brown
    #
    # # declare y_shift
    # y_shift = 135
    #
    # # declare number of total rows
    # row_total = 6
    #
    # # declare all other rows
    # for i in range(1, row_total):
    #
    #     chips.append(pcv.roi.rectangle(img=img, x= 940, y=1400 + i * (y_shift), w=dimensions[0], h=dimensions[1]))
    #     chips.append(pcv.roi.rectangle(img=img, x=1080, y=1400 + i * (y_shift), w=dimensions[0], h=dimensions[1]))
    #     chips.append(pcv.roi.rectangle(img=img, x=1230, y=1400 + i * (y_shift), w=dimensions[0], h=dimensions[1]))
    #     chips.append(pcv.roi.rectangle(img=img, x=1390, y=1400 + i * (y_shift), w=dimensions[0], h=dimensions[1]))
    #
    # # remove black and white
    # del chips[0]
    # del chips[19]
    #
    # mask = np.zeros(shape=np.shape(img)[:2], dtype=np.uint8())  # create empty mask img.
    #
    # i = 1
    # for chip in chips:
    #     print(chip)
    #     mask = cv2.drawContours(mask, chip[0], -1, (i * 10), -1)
    #     i += 1
    #
    # #mask = mask * 10  # multiply values in the mask for greater contrast. Exclude if designating have more than 25 color chips.
    # pcv.plot_image(mask)
    # cv2.imwrite("img/test_mask.jpg", mask)  # write to file.
    # print("finaliza",chips[10])