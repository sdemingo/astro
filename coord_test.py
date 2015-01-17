

from coord import *


def main():

    print ("Conversion de Horizontales a horarias: Ejemplo 1")
    A=Angle()
    h=Angle()
    fi=Angle()
    A.setSexagesimal(210,34,0)
    h.setSexagesimal(35,43,0)
    fi.setSexagesimal(3,25,0)

    d,H=horizontales2horarias(A,h,fi)

    print ("delta:",d)
    print ("H:",H)


    print ("\n\nConversion de Horizontales a horarias: Ejemplo 2")
    A=Angle()
    h=Angle()
    fi=Angle()
    A.setSexagesimal(47,34,0)
    h.setSexagesimal(67,45,0)
    fi.setSexagesimal(-17,-36,-0) # negativo porque es latitud Sur
    d,H=horizontales2horarias(A,h,fi)

    print ("delta:",d)
    print ("H:",H)


    print ("\n\nConversion de Horarias a horizontales: Ejemplo 1")
    H=Angle()
    delta=Angle()
    fi=Angle()
    H.setSexagesimal(83,49.5,0)
    delta.setSexagesimal(34,14,0)
    fi.setSexagesimal(1,9,0)

    h,A=horarias2horizontales(delta,H,fi)

    print ("h:",h)
    print ("A:",A)



    print ("\n\nConversion de eclípticas a absolutas: Ejemplo 1")
    beta=Angle()
    lamb=Angle()
    epsilon=Angle()
    beta.setSexagesimal(4,54)
    lamb.setSexagesimal(221,23)
    epsilon.setSexagesimal(23,26)

    alfa,delta=eclipticas2absolutas(beta,lamb,epsilon)

    print("alfa: ",alfa)
    print("delta: ",delta)


    print ("\n\nConversion de eclípticas a absolutas: Ejemplo 2")
    beta=Angle()
    lamb=Angle()
    epsilon=Angle()
    beta.setSexagesimal(0,0)
    lamb.setSexagesimal(325,36)
    epsilon.setSexagesimal(23,26)

    alfa,delta=eclipticas2absolutas(beta,lamb,epsilon)

    print("alfa: ",alfa)
    print("delta: ",delta)


    print ("\n\nConversion de absolutas a eclípticas: Ejemplo 1")
    alfa=Angle()
    delta=Angle()
    epsilon=Angle()
    alfa.setSexagesimal(81,52.5)
    delta.setSexagesimal(19,45)
    epsilon.setSexagesimal(23,26)

    lamb,beta=absolutas2eclipticas(alfa,delta,epsilon)

    print("beta: ",beta)
    print("lambda: ",lamb)


    print ("\n\nConversion de absolutas a eclípticas: Ejemplo 2")
    alfa=Angle()
    delta=Angle()
    epsilon=Angle()
    alfa.setSexagesimal(187,27,18.15)
    delta.setSexagesimal(-3,-13,-9.6)
    epsilon.setSexagesimal(23,26,18.50)

    lamb,beta=absolutas2eclipticas(alfa,delta,epsilon)

    print("beta: ",beta)
    print("lambda: ",lamb)


    print ("\n\nObtención de medias por corrección de precesión:")
    # Página 181 del Portilla
    alfa=Angle()
    delta=Angle()
    alfa.setHours(6,23,57.119)
    delta.setSexagesimal(-52,-41,-44.5)

    print ("alfa0: ",alfa)
    print ("delta0: ",delta)

    a1,d1=correcPrecesion(alfa,delta,"8.5.2010")
    
    #Coordenadas ecuatoriales para equinocio medio del dia en cuestión
    print ("alfa:",a1)
    print ("delta:",d1)


    print ("\n\nObtención de verdaderas por corrección de nutación:")
    # Página 184 del Portilla
    alfa=Angle()
    delta=Angle()
    alfa.setHours(6,23,57.119)
    delta.setSexagesimal(-52,-41,-44.5)

    print ("alfa0: ",alfa)
    print ("delta0: ",delta)

    a1,d1=correcPrecesion(alfa,delta,"8.5.2010")
    a2,d2=correcNutacion(a1,d1,"8.5.2010")
    
    print ("alfa:",a2.getHours())
    print ("delta:",d2)
 
 




if (__name__=='__main__'):
    main()
