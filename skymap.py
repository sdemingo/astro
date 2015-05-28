#!/usr/bin/python
# -*- coding: utf-8 -*- 



from matplotlib.pyplot import rc, grid, figure, rcParams, savefig, show, plot
from math import radians
import itertools 

import numpy as np
import datetime

import tiempo
from sol import *




def plot_points(fig,points,edge,color='b'):
    x=[]
    y=[]
    for (E, Az) in points:
        if E > 0:
            x.append(radians(Az))
            y.append(90-E)


    ax1 = fig.add_subplot(111, polar=True, axisbg='white')
    ax1.set_theta_zero_location('N')
    ax1.set_theta_direction(-1)

    style=' '
    if edge:
        style='-'

    ax1.plot(x,y,color,marker='.',linestyle=style)
    ax1.set_yticks(range(0, 90+10, 10))
    ax1.set_yticklabels([])



