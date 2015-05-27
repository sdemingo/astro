#!/usr/bin/python
# -*- coding: utf-8 -*- 



from matplotlib.pyplot import rc, grid, figure, rcParams, savefig, show, plot
from math import radians

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

    ax1.plot(x,y,color,marker='o',linestyle=' ')
    ax1.set_yticks(range(0, 90+10, 10))
    ax1.set_yticklabels([])




 



def main():
    obs = ephem.Observer()
    obs.lat = ephem.degrees(str(LATITUD))
    obs.lon = ephem.degrees(str(LONGITUD))
    pos_v=[]
    pos_i=[]


    for h in range(0,23):
        day = datetime.strptime("21.12.2014",day_format)

        if h < 10:
            sdate = day.strftime("%Y/%m/%d")+" 0"+str(h)+":00"
        else:
            sdate = day.strftime("%Y/%m/%d")+" "+str(h)+":00"

        obs.date = sdate
        star = ephem.Sun()
        star.compute(obs)
        pos_i.append([math.degrees(star.alt),math.degrees(star.az)])




    for h in range(0,23):
        day = datetime.strptime("21.6.2015",day_format)

        if h < 10:
            sdate = day.strftime("%Y/%m/%d")+" 0"+str(h)+":00"
        else:
            sdate = day.strftime("%Y/%m/%d")+" "+str(h)+":00"
            
        obs.date = sdate
        star = ephem.Sun()
        star.compute(obs)
        pos_v.append([math.degrees(star.alt),math.degrees(star.az)])
    



    # Dibujo la gráfica
    fig = figure()
    plot_points(fig,pos_i)
    plot_points(fig,pos_v,'r')
    show()





if (__name__=='__main__'):
    main()


