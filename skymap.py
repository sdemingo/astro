#!/usr/bin/python
# -*- coding: utf-8 -*- 



from matplotlib.pyplot import rc, grid, figure, plot, rcParams, savefig, show
from math import radians

import numpy as np
import datetime

import tiempo
from sol import *


alturas=[]
azimuts=[]
day=datetime(2015, 6, 1) 


def plot_positions(observer_lat, observer_lon, positions):

    width, height = rcParams['figure.figsize']
    size = min(width, height)
    fig = figure(figsize=(size, size))

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True, axisbg='white')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    x=[]
    y=[]
    for (E, Az) in positions:
        if E > 0:
            x.append(radians(Az))
            y.append(90-E)

    plot(x,y,color='b',marker='o',linestyle=' ')
    ax.set_yticks(range(0, 90+10, 10))
    ax.set_yticklabels([])
    grid(True)




def main():

    obs = ephem.Observer()
    obs.lat = ephem.degrees(str(LATITUD))
    obs.lon = ephem.degrees(str(LONGITUD))
    pos=[]


    for h in range(0,23):
        day = datetime.strptime("21.12.2014",day_format)

        if h < 10:
            sdate = day.strftime("%Y/%m/%d")+" 0"+str(h)+":00"
        else:
            sdate = day.strftime("%Y/%m/%d")+" "+str(h)+":00"

        obs.date = sdate
        star = ephem.Sun()
        star.compute(obs)
        pos.append([math.degrees(star.alt),math.degrees(star.az)])




    for h in range(0,23):
        day = datetime.strptime("21.6.2015",day_format)

        if h < 10:
            sdate = day.strftime("%Y/%m/%d")+" 0"+str(h)+":00"
        else:
            sdate = day.strftime("%Y/%m/%d")+" "+str(h)+":00"
            
        obs.date = sdate
        star = ephem.Sun()
        star.compute(obs)
        pos.append([math.degrees(star.alt),math.degrees(star.az)])
    

    plot_positions(obs.lat,obs.lon,pos)
    show()





if (__name__=='__main__'):
    main()


