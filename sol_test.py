# -*- coding: utf-8 -*- 

from sol import *
import matplotlib.pyplot as plt
from numpy import *



def datos(fecha,hora):
    print "Ecuación de tiempo: "+ str(ecuacionTiempo(fecha))
    print "Tiempo solar: "+ str(tiempoSolar(fecha,hora))
    print "Mediodía: "+ str(mediodiaCivil(fecha))
    print "--------------"
    print "Angulo horario: "+ str(anguloHorario(fecha,hora))
    print "Declinacion: "+str(declinacion(fecha2ordinal(fecha)))
    print "--------------"
    print "Altitud: "+str(altitud(fecha,hora))
    print "Azimut: "+str(azimut(fecha,hora))
    print "--------------"
    medio=mediodiaCivil(fecha)
    medio_s=medio.strftime(hour_format)
    print "Max. Altitud al mediodia: "+str(altitud(fecha,medio_s))  



def grafica():
    
    alturas=[]
    for i in range(1,366):
        day=datetime(2015, 1, 1) + timedelta(i - 1)
        sday=day.strftime(day_format)
        mday=mediodiaCivil(sday)
        smday=mday.strftime(hour_format)
        alturas.append(altitud(sday,smday))
        
    x = range(1,366)
    y1 = alturas

    plt.plot(x,y1,color='b')
    plt.xlim(1,365)
    plt.title(u'Altura del Sol sobre el horizonte')
    plt.xlabel(u'Días')
    plt.xticks(linspace(1,365,5))
    plt.grid()
    plt.axhline(0, color='black')
    plt.show()    
        


    

def main():
    #datos("22.1.2015","20:39")
    grafica()






if (__name__=='__main__'):
    main()
