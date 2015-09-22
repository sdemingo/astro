#!/usr/bin/python
# -*- coding: utf-8 -*- 



from matplotlib.pyplot import rc, grid, figure, rcParams, savefig, show, plot
from math import radians
import itertools 

import numpy as np
import datetime

import tiempo
from sol import *




class Catalog:

    def __init__(self,filename):
        self.stars={}
        file = open(filename, "r")
        for line in file.readlines():
            key=line.split(",")[0]
            self.stars[key]=line[:len(line)-1]
            

    


class Constellation:
    
    def __init__(self,obs,catalog):
        self.stars={}
        self.points={}
        self.catalog = catalog
        self.observer = obs


    def add_edge(self,fig,sname1, sname2, color='b'):

        # if the stars name (sname1 or sname2)  are not defined in the
        # default set of  pyephem it uses the external catalog

        if (sname1 not in self.stars):
            try:
                s1=ephem.star(sname1)
                s1.compute(self.observer)
            except:
                s1=ephem.readdb(self.catalog.stars[sname1])
                s1.compute(self.observer)
 
            p1=[math.degrees(s1.alt), math.degrees(s1.az)]
            self.stars[sname1]=s1
            self.points[sname1]=p1

        if (sname2 not in self.stars):
            try:
                s2=ephem.star(sname2)
                s2.compute(self.observer)
            except:
                s2=ephem.readdb(self.catalog.stars[sname2])
                s2.compute(self.observer)

            p2=[math.degrees(s2.alt), math.degrees(s2.az)]
            self.stars[sname2]=s2
            self.points[sname2]=p2

        self.__plot_points__(fig,[self.points[sname1],self.points[sname2]],color)

    
    def add_star(self,fig,sname1, color='b'):
        if (sname1 not in self.stars):
            s1=ephem.star(sname1)
            s1.compute(self.observer)
            p1=[math.degrees(s1.alt), math.degrees(s1.az)]
            self.stars[sname1]=s1
            self.points[sname1]=p1

        self.__plot_points__(fig,[self.points[sname1]],color)






    def __plot_points__(self,fig,points,color):
        x=[]
        y=[]
        for (E, Az) in points:
            if E > 0:
                x.append(radians(Az))
                y.append(90-E)

        ax1 = fig.add_subplot(111, polar=True, axisbg='white')
        ax1.plot(x,y,color,marker='.',linestyle="-")






def showGraph(fig):
    ax1 = fig.add_subplot(111, polar=True, axisbg='white')
    ax1.set_theta_zero_location('N')
    ax1.set_theta_direction(-1)

    ax1.set_yticks(range(0, 90+10, 10))
    ax1.set_yticklabels([])

    show()

