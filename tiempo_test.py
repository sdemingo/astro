#!/usr/bin/python
# -*- coding: utf-8 -*- 


import matplotlib.pyplot as plt
from tiempo import *
from numpy import *


def main():
    
    res1=[]
    for i in range(1,366):
        res1.append(ecuacionTiempo3(i))

    x = range(1,366)
    y1 = res1

    plt.plot(x,y1,color='b')
    plt.ylim(-17,+17)
    plt.xlim(1,365)
    plt.title(u'Ecuación de tiempo')
    plt.ylabel('minutos')
    plt.xlabel(u'días')
    plt.xticks(linspace(1,365,5))
    plt.grid()
    plt.axhline(0, color='black')
    plt.show()

  



if (__name__=='__main__'):
    main()

