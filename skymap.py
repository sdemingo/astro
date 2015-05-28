#!/usr/bin/python
# -*- coding: utf-8 -*- 



from matplotlib.pyplot import rc, grid, figure, rcParams, savefig, show, plot
from math import radians
import itertools 

import numpy as np
import datetime

import tiempo
from sol import *




def plot_points(fig,points,color='b'):
    x=[]
    y=[]
    for (E, Az) in points:
        if E > 0:
            x.append(radians(Az))
            y.append(90-E)


    ax1 = fig.add_subplot(111, polar=True, axisbg='white')
    ax1.set_theta_zero_location('N')
    ax1.set_theta_direction(-1)

    ax1.plot(x,y,color,marker='.',linestyle=' ')
    ax1.set_yticks(range(0, 90+10, 10))
    ax1.set_yticklabels([])




def plot_graph(fig,pairs,color='b'):
            
    ax=fig.add_subplot(111, polar=True, axisbg='white')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    for point in pairs:
        for point2 in pairs:
            plot([point[0], point2[0]], [point[1], point2[1]],color,marker='o')

    ax.set_yticks(range(0, 90+10, 10))
    ax.set_yticklabels([])

    

