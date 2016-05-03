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

    horario_verano = datetime(2015, 3, 28)
    horario_invierno = datetime(2015, 10, 24)
    
    ortos_utc=[]
    ortos_gmt=[]

    ocasos_utc=[]
    ocasos_gmt=[]
    for i in range(1,366):
        day=datetime(2015, 1, 1) + timedelta(i - 1)
        sday=day.strftime(day_format)

        ort=orto(sday)
        ort_utc_hours = (ort  - ort.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
        ortos_utc.append(ort_utc_hours)
        if (day < horario_verano) or (day > horario_invierno):
            ortos_gmt.append(ort_utc_hours+1)
        else:
            ortos_gmt.append(ort_utc_hours+2)

        ocs=ocaso(sday)
        ocs_utc_hours = (ocs - ocs.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
        ocasos_utc.append(ocs_utc_hours)
        if (day < horario_verano) or (day > horario_invierno):
            ocasos_gmt.append(ocs_utc_hours+1)
        else:
            ocasos_gmt.append(ocs_utc_hours+2)

    
    x = range(1,366)
    y1 = ortos_utc
    y2 = ocasos_utc
    y3 = ortos_gmt
    y4 = ocasos_gmt

    c1 = "#3399FF"  #blue
    c2 = "#CC0000"  #red
    c3 = "#004C99"  #dark blue
    c4 = "#660000"  #dark red

    plt.plot(x,y1,linewidth=1.0,c=c1,label="orto UTC")
    plt.plot(x,y2,linewidth=1.0,c=c2,label="ocaso UTC")
    plt.plot(x,y3,linewidth=2.5,c=c3,label="orto GMT")  
    plt.plot(x,y4,linewidth=2.5,c=c4,label="ocaso GMT")


    plt.xlim(1,365)
    plt.ylim(0,24)
    plt.title(u'Orto y ocaso del Sol')
    plt.xlabel(u'Días')
    plt.ylabel(u'Horas')
    plt.xticks(linspace(1,365,5))
    plt.yticks(linspace(0,23,24))
    plt.grid()

    plt.legend(loc='lower left',fontsize=10)

    plt.axhline(0, color='black')
    plt.axhspan(8, 20, alpha=0.5, color="#C0C0C0")

    plt.show()    

    








def main():
    datos("22.5.2015","20:39")
    #grafica()
    #grafica2()






if (__name__=='__main__'):
    main()
