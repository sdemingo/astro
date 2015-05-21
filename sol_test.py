# -*- coding: utf-8 -*- 

from sol import *
import matplotlib.pyplot as plt
from numpy import *



def datos(fecha,hora):
    print "Ecuación de tiempo: "+ str(ecuacionTiempo(fecha))
    print "Tiempo solar: "+ str(tiempoSolar(fecha,hora))
    print "Mediodía: "+ str(mediodiaCivil(fecha))
    print "Orto: "+str(orto(fecha))
    print "Ocaso: "+str(ocaso(fecha))
    print "Horas de Luz: "+str(minutosDeLuz(fecha)/60)
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




#
# Altura del Sol sobre el horizonte
#

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
    



#
# Orto y ocaso del Sol durante el año
#

def grafica2():
    
    ortos=[]
    ocasos=[]
    for i in range(1,366):
        day=datetime(2015, 1, 1) + timedelta(i - 1)
        sday=day.strftime(day_format)

        ort=orto(sday)
        ort_hours = (ort  - ort.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
        ortos.append(ort_hours)

        ocs=ocaso(sday)
        ocs_hours = (ocs - ocs.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
        ocasos.append(ocs_hours)

    
    x = range(1,366)
    y1 = ortos
    y2 = ocasos

    plt.plot(x,y1,'b',x,y2,'r')
    plt.xlim(1,365)
    plt.ylim(0,24)
    plt.title(u'Orto y ocaso del Sol')
    plt.xlabel(u'Días')
    plt.ylabel(u'Hora')
    plt.xticks(linspace(1,365,5))
    plt.grid()
    plt.axhline(0, color='black')
    plt.show()    

    








def main():
    #datos("21.5.2015","20:39")
    #grafica()
    grafica2()






if (__name__=='__main__'):
    main()
