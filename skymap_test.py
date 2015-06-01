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
    ursae = Constellation(obs)
    ursae.add_edge(fig,"Merak","Dubhe")
    ursae.add_edge(fig,"Merak","Phecda")
    ursae.add_edge(fig,"Dubhe","Megrez")
    ursae.add_edge(fig,"Megrez","Phecda")
    ursae.add_edge(fig,"Alioth","Megrez")
    ursae.add_edge(fig,"Alioth","Mizar")
    ursae.add_edge(fig,"Mizar","Alcaid")



    # Dibujo estrella polar
    polaris = Constellation(obs)
    polaris.add_star(fig,"Polaris","red")
    

   
    # Dibujo el gráfico entero
    showGraph(fig)





if (__name__=='__main__'):
    main()


