#!/usr/bin/python
# -*- coding: utf-8 -*- 



from tiempo import *



def main():

    for i in range(1,365):
        et1=ecuacionTiempo1(i)
        et2=ecuacionTiempo2(i)
        et3=ecuacionTiempo3(i)
        et4=ecuacionTiempo4(i)
        print (i, et1,et2,et3,et4)




if (__name__=='__main__'):
    main()

