# -*- coding: utf-8 -*- 

from sol import *

def main():

    fecha="22.1.2015"
    hora="20:39"
    
    print "Ecuación de tiempo: "+ str(ecuacionTiempo3(fecha2ordinal(fecha)))
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






if (__name__=='__main__'):
    main()
