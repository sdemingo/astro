#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''
Ecuaciones de tiempo extraidas de: Spline-Based Formulas for the
Determination of Equation of Time and Declination Angle - Fawzi
Al-Naima and Bilal Abdul Majeed.

Las ecuaciones de tiempo resumidas en el articulo estan citadas (por
orden) en: :

[1] P. J. Lunde, Solar Thermal Engineering—Space Heating and Hot Water
    Systems, John Wiley & Sons, New York, NY, USA, 1980.
[2] M. Iqbal, An Introduction to Solar Radiations, Academic Press, New
    York, NY, USA, 1986.
[3] J. Kennewell and A. McDonald, “The equation of time,” Australian
    Government, ISP-Radio and Space Services, http://www.ips.gov.au/.
[4] G. M. Masters, Renewable and Efficient Electric Power Systems,
    John Wiley & Sons, New York, NY, USA, 2004.  
'''

from math import *
from datetime import *


day_format='%d.%m.%Y'
hour_format='%H:%M'


def ecuacionTiempo1(n):
    if (n<100):
        return -9*sin((n-1)/28.648) - 5
    if (n>=100) and (n<=242):
        return -5*sin((n-100)/22.632) - 1
    if (n>242):
        return -18.6*sin((n-242)/39.248) - 2

def ecuacionTiempo2(n):
    w= (2*pi*(n-1))/365
    a=0.000075
    b=0.001868*cos(w)
    c=0.032077*sin(w)
    d=0.014615*cos(w)
    e=0.04089*sin(2*w)
    et=229.18*(a+b-c-d-e)
    return et

def ecuacionTiempo3(n):
    b= (360*(n-81))/365
    return 9.87 * sin(radians(2*b)) - 7.67*sin(radians(b + 78.7))


def ecuacionTiempo4(n):
    b= (360*(n-81))/365
    return 9.87 * sin(radians(2*b)) - 7.53*cos(radians(b)) - 1.5*sin(radians(b))



def tdelta(t):
    aet=abs(t)
    mint=int(aet)
    secs=int((aet-mint)*60)
    return timedelta(minutes=mint,seconds=secs)



def diaJuliano(dia):
    dt = datetime.strptime(dia, day_format)
    a = (14 - dt.month)//12
    y = dt.year + 4800 - a
    m = dt.month + 12*a - 3
    return dt.day + ((153*m + 2)//5) + 365*y + y//4 - y//100 + y//400 - 32045



def diaOrdinal(dia):   # retorna un ordinal de año (1-365) en base a una fecha
    dt = datetime.datetime.strptime(dia, day_format)
    tt = dt.timetuple()
    return tt.tm_yday
