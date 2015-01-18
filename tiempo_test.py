#!/usr/bin/python
# -*- coding: utf-8 -*- 


import matplotlib.pyplot as plt
from tiempo import *
from numpy import *


def main():
    
    res1=[]
    res2=[]
    res3=[]
    for i in range(1,366):
        res1.append(ecuacionTiempo1(i))
        res2.append(ecuacionTiempo2(i))
        res3.append(ecuacionTiempo3(i))
        # et1=ecuacionTiempo1(i)
        # et2=ecuacionTiempo2(i)
        # et3=ecuacionTiempo3(i)
        # print (i, et1,et2,et3)


    x = range(1,366)
    y1 = res1
    y2 = res2
    y3 = res3
    plt.plot(x,y1,color='r')
    plt.plot(x,y2,color='b')
    #plt.plot(x,y3,color='g')
    plt.ylim(-17,+17)
    plt.xlim(1,365)
    plt.ylabel('minutos')
    plt.xticks(linspace(1,365,5))
    plt.show()

  



if (__name__=='__main__'):
    main()

