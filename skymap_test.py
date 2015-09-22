#!/usr/bin/python
# -*- coding: utf-8 -*- 


from skymap import *



def main():

    # Based on the 5th Revised edition of the Yale Bright 
    # Star Catalog, 1991, from
    # ftp://adc.gsfc.nasa.gov/pub/adc/archives/catalogs/5/5050.

    cat = Catalog("YBS.edb")
    
    obs = ephem.Observer()
    obs.lat = ephem.degrees(str(LATITUD))
    obs.lon = ephem.degrees(str(LONGITUD))
    obs.date = "1/6/2015 5:00"


    fig = figure()

    # Dibujo osa mayor
    ursae = Constellation(obs,cat)
    ursae.add_edge(fig,"Merak","Dubhe")
    ursae.add_edge(fig,"Merak","Phecda")
    ursae.add_edge(fig,"Dubhe","Megrez")
    ursae.add_edge(fig,"Megrez","Phecda")
    ursae.add_edge(fig,"Alioth","Megrez")
    ursae.add_edge(fig,"Alioth","Mizar")
    ursae.add_edge(fig,"Mizar","Alcaid")

    # Dibujo draco
    draco = Constellation(obs,cat)
    draco.add_edge(fig,"Dra Kappa","Dra Lambda")
    draco.add_edge(fig,"Dra Alpha","Dra Kappa")
    draco.add_edge(fig,"Dra Alpha","Dra Iota")
    draco.add_edge(fig,"Dra Theta","Dra Iota")
    draco.add_edge(fig,"Dra Theta","Dra Eta")
    draco.add_edge(fig,"Dra Zeta","Dra Eta")
    draco.add_edge(fig,"Dra Zeta","Dra Chi")
    draco.add_edge(fig,"Dra Epsilon","Dra Chi")
    draco.add_edge(fig,"Dra Epsilon","Dra Delta")
    draco.add_edge(fig,"Dra Xi","Dra Delta")
    draco.add_edge(fig,"Dra Xi","Dra Nu1")
    draco.add_edge(fig,"Dra Beta","Dra Nu1")
    draco.add_edge(fig,"Dra Beta","Dra Gamma")
    draco.add_edge(fig,"Dra Xi","Dra Gamma")

    # Dibujo estrella polar
    polaris = Constellation(obs,cat)
    polaris.add_star(fig,"Polaris","red")
    

   
    # Dibujo el gráfico entero
    showGraph(fig)





if (__name__=='__main__'):
    main()


