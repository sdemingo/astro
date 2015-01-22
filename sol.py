# -*- coding: utf-8 -*- 


'''
Referencias
[1] Solar Energy Engineering: Processes and Systems - Soteris A. Kalogirou
'''

from math import *
from numpy import *
import datetime
from tiempo import *


LATITUD=40.417086  
LONGITUD=-3.703507


def declinacion(n):
    i=((2*pi)*(n-1))/365.0
    dec=0.006918-(0.399912*cos(i))+(0.070257*sin(i))-(0.006758*cos(2*i))+(0.000907*sin(2*i))-(0.002697*cos(3*i))+(0.00148*sin(3*i))
    return degrees(dec)



def ecuacionTiempo(dia):
    et=ecuacionTiempo1(fecha2ordinal(dia))
    aet=abs(et)
    mint=int(aet)
    secs=int((aet-mint)*60)
    tet = timedelta(minutes=mint,seconds=secs)

    return (et,tet)

def fecha2ordinal(dia):   # retorna un ordinal de año (1-365) en base a una fecha
    dt = datetime.strptime(dia, day_format)
    tt = dt.timetuple()
    return tt.tm_yday
    

def tiempoSolar(dia,hora): 
    h = datetime.strptime(hora, hour_format)
    lst=h  #tiempo civil
    lstm= 15.0*(LONGITUD/15.0) # longitud local sobre el tiempo de meridiano
    et,tet=ecuacionTiempo(dia)  
    corr=timedelta(minutes=int(4*(lstm + LONGITUD)))  #correcion sobre el meridiano
    dl_saving=timedelta(hours=1)  # adelanto de verano/invierno

    ast=lst + corr + tet - dl_saving
    return ast



def mediodiaCivil(dia): 
    h = datetime.strptime("12:00", hour_format)
    lst=h  #tiempo solar
    lstm= 15.0*(LONGITUD/15.0) # longitud local sobre el tiempo de meridiano
    et,tet=ecuacionTiempo(dia)  
    corr=timedelta(minutes=int(4*(lstm + LONGITUD)))  #correcion sobre el meridiano
    dl_saving=timedelta(hours=1)  # adelanto de verano/invierno

    ct=lst - corr - tet + dl_saving  #tiempo civil
    return ct


def decimalHour(hora):
    HMS = [60*60, 60, 1]
    dec_time = sum(a * b for a,b in zip(HMS, map(int, hora.split(":"))))
    dec_time /= 3600.
    return dec_time


def anguloHorario(dia,hora):
    ast=tiempoSolar(dia,hora)
    ast_decimal=decimalHour(ast.strftime(hour_format))
    return (ast_decimal-12)*15



def altitud(dia,hora):
    h=anguloHorario(dia,hora)
    dec=declinacion(fecha2ordinal(dia))
    return degrees(arcsin((cos(radians(LATITUD))*cos(radians(dec))*cos(radians(h))) + (sin(radians(LATITUD))*sin(radians(dec)))))



def azimut(dia,hora):
    h=anguloHorario(dia,hora)
    dec=declinacion(fecha2ordinal(dia))
    alt=altitud(dia,hora)
    return degrees(arcsin((cos(radians(dec))*sin(radians(h)))/cos(radians(alt))))

