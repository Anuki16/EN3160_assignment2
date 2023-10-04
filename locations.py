# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:03:34 2023

@author: anuki
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img3 = cv.imread("images/street.jfif")
img3 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)

logo = cv.imread("images/fide.png")
logo = cv.cvtColor(logo, cv.COLOR_BGR2RGB)

source_points = [(3, 1109), (275, 912), (663, 912), (974, 1242)]
source_points = np.array([np.array(p) for p in source_points])

plt.imshow(img3)
plt.show()

def onclick(event):
    ix, iy = event.xdata, event.ydata
    plt.scatter(ix, iy, color='red')
    plt.gcf().canvas.draw()
    print(f'x = {ix}, y = {iy}')

cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)