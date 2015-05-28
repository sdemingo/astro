#!/usr/bin/python
# -*- coding: utf-8 -*- 


from skymap import *


def main():
    obs = ephem.Observer()
    obs.lat = ephem.degrees(str(LATITUD))
    obs.lon = ephem.degrees(str(LONGITUD))
    obs.date = "1/6/2015 5:00"


    fig = figure()

    # Dibujo osa mayor
    ursae = [ephem.star("Merak"),
              ephem.star("Dubhe"),
              ephem.star("Phecda"),
              ephem.star("Megrez"),
              ephem.star("Alioth"),
              ephem.star("Mizar"),
              ephem.star("Alcaid")]

    ursae_points=[]
    for s in ursae:
         s.compute(obs)
         ursae_points.append([math.degrees(s.alt),math.degrees(s.az)])
    plot_points(fig,ursae_points)


    # Dibujo estrella polar
    polaris = ephem.star("Polaris")
    polaris.compute(obs)
    polaris_points = [[math.degrees(polaris.alt),math.degrees(polaris.az)]]
    plot_points(fig,polaris_points)


   
    show()



if (__name__=='__main__'):
    main()


