

from math import *
from ascalendar import *

class Angle:
    def __init__(self,d=0,m=0,s=0):
        self.d=0
        self.m=0
        self.s=0
        self.dec=0

    def setSexagesimal(self,d,m=0,s=0):
        self.d=d
        self.m=m
        self.s=s
        self.dec=self.d + self.m/60 + self.s/3600

    def setDecimal(self,dec):
        self.dec=dec
        (hfrac, self.d) = modf(self.dec)
        (min_frac, self.m) = modf(hfrac * 60)
        self.s = min_frac * 60


    def setRadians(self,rad):
        self.dec=rad*180
        (hfrac, self.d) = modf(self.dec)
        (min_frac, self.m) = modf(hfrac * 60)
        self.s = min_frac * 60

    def setHours(self,h,m=0,s=0):
        hours=h + m/60 + s/3600
        dec=(hours*360)/24

        self.dec=dec
        (hfrac, self.d) = modf(self.dec)
        (min_frac, self.m) = modf(hfrac * 60)
        self.s = min_frac * 60

    def getDecimal(self):
        return self.dec

    def getSexagesimal(self):
        return (self.d,self.m,self.s)

    def getRadians(self):
        return radians(self.dec)

    def getHours(self):
        degrees=self.d + self.m/60 + self.s/3600
        hours=(degrees*24)/360

        (hfrac, h) = modf(hours)
        (min_frac, m) = modf(hfrac * 60)
        s = min_frac * 60

        return (int(h), int(m), s)

    def __str__(self):
        return "{0}º {1}' {2}''".format(int(self.d),int(self.m),self.s)



def HrA(h,m=0,s=0):
    a=Angle()
    a.setHours(h,m,s)
    return a

def SgA(d,m=0,s=0):
    a=Angle()
    a.setSexagesimal(d,m,s)
    return a

def DcA(d):
    a=Angle()
    a.setDecimal(d)
    return a



EPSILON=SgA(23,26,21.4)


def horizontales2horarias(a_A,a_h,a_fi):
    A=a_A.getRadians()
    h=a_h.getRadians()
    fi=a_fi.getRadians()
    delta=asin((sin(fi)*sin(h))+(cos(fi)*cos(h)*cos(A)))
    delta=degrees(delta)

    H=asin(((-1)*(cos(h)*sin(A))) / (cos(radians(delta))))
    H=degrees(H)
    Ad=degrees(A)

    a_delta=Angle()
    a_H=Angle()
    a_delta.setDecimal(delta)
    a_H.setDecimal(H)

    return a_delta,a_H


def horarias2horizontales(a_delta,a_H,a_fi):
    delta=a_delta.getRadians()
    H=a_H.getRadians()
    fi=a_fi.getRadians()

    h=asin((sin(delta)*sin(fi)) + (cos(delta)*cos(fi)*cos(H)))
    A=asin(( -cos(delta)*sin(H)) / cos(h))

    a_h=Angle()
    a_A=Angle()
    if (a_H.getDecimal()<180):
        a_h.setDecimal(degrees(h)),a_A.setDecimal(360-abs(degrees(A)))
    else:
        a_h.setDecimal(degrees(h)),a_A.setDecimal(degrees(A))

    return a_h,a_A



def eclipticas2absolutas(a_beta,a_lambda,epsilon):
    beta=a_beta.getRadians()
    lamb=a_lambda.getRadians()
    eps=epsilon.getRadians()

    delta=asin((sin(beta)*cos(eps))+(cos(beta)*sin(eps)*sin(lamb)))

    p=((-sin(beta)*sin(eps))+(cos(beta)*cos(eps)*sin(lamb)))
    q=(cos(lamb)*cos(beta))
    alfa=atan( p / q )

    a_delta=Angle()
    a_alfa=Angle()
    if ((p*q)<0) and (q<0):
        a_alfa.setDecimal(degrees(alfa)+180),a_delta.setDecimal(degrees(delta))
        return a_alfa,a_delta

    if ((p*q)<0) and (q>0):
        a_alfa.setDecimal(degrees(alfa)+360),a_delta.setDecimal(degrees(delta))
        return a_alfa,a_delta

    if (p+q)<0:
        a_alfa.setDecimal(degrees(alfa)+180),a_delta.setDecimal(degrees(delta))
        return a_alfa,a_delta

    a_alfa.setDecimal(degrees(alfa)),a_delta.setDecimal(degrees(delta))
    return a_alfa,a_delta




def absolutas2eclipticas(a_alfa,a_delta,epsilon):
    alfa=a_alfa.getRadians()
    delta=a_delta.getRadians()
    eps=epsilon.getRadians()

    beta=asin((sin(delta)*cos(eps))-(cos(delta)*sin(eps)*sin(alfa)))

    p=((sin(delta)*sin(eps))+(cos(delta)*cos(eps)*sin(alfa)))
    q=(cos(alfa)*cos(delta))
    lamb=atan( p / q )

    a_beta=Angle()
    a_lamb=Angle()

    if ((p*q)<0) and (q<0):
        a_lamb.setDecimal(degrees(lamb)+180),a_beta.setDecimal(degrees(beta))
        return a_lamb,a_beta

    if ((p*q)<0) and (q>0):
        a_lamb.setDecimal(degrees(lamb)+360),a_beta.setDecimal(degrees(beta))
        return a_lamb,a_beta

    if (p+q)<0:
        a_lamb.setDecimal(degrees(lamb)+180),a_beta.setDecimal(degrees(beta))
        return a_lamb,a_beta

    a_lamb.setDecimal(degrees(lamb)),a_beta.setDecimal(degrees(beta))
    return a_lamb,a_beta



def correcPrecesion(alfa,delta,date):
    # for epoch J2000.0
    #  T= (JulianDate) − 2451545.0) / 36525

    jd=julianDay(date)
    t=(jd - 2451545.0) / 36525

    m=(1.281232*t)+(3.879e-4*(t**2))+(1.101e-5*(t**3))
    n=(0.5567530*t)-(1.185e-4*(t**2))-(1.16e-5*(t**3))

    alfa_aux= alfa.getDecimal()+(0.5*(m+(n*sin(alfa.getRadians())*tan(delta.getRadians()))))
    delta_aux= delta.getDecimal()+(0.5*(n*cos(alfa.getRadians())))

    alfa_m=alfa.getDecimal() + m + (n*sin(alfa.getRadians())*tan(delta.getRadians()))
    delta_m=delta.getDecimal() + (n*cos(alfa.getRadians()))
    
    alfa_a=Angle()
    delta_a=Angle()
    alfa_a.setDecimal(alfa_m)
    delta_a.setDecimal(delta_m)

    return alfa_a,delta_a



def correcNutacion(alfa,delta,date):
    # Página 183 del Portilla
    # Corrección de precisión media (en torno a un segundo de arco)
    
    jd=julianDay(date)
    t=(jd - 2451545.0) / 36525

    om = (125.04 - (1934.13*t))%360
    d = (297.85 + (445267.11*t))%360
    f = (93.27 + (483202.0175*t))%360

    om_a=DcA(om)
    d_a=DcA(d)
    f_a=DcA(f)

    incOm_1= SgA(0,0,-17.2).getDecimal()*sin(om_a.getRadians())
    incOm_2= SgA(0,0,0.2).getDecimal()*sin(2*om_a.getRadians())
    incOm_3= SgA(0,0,-1.3).getDecimal()*sin((2*om_a.getRadians())+(2*f_a.getRadians())-(2*d_a.getRadians()))
    incOm_4= SgA(0,0,-0.2).getDecimal()*sin((2*om_a.getRadians())+(2*f_a.getRadians()))
    incOm= incOm_1 + incOm_2 - incOm_3 + incOm_4

    incEp_1= SgA(0,0,9.2).getDecimal()*cos(om_a.getRadians())
    incEp_2= SgA(0,0,-0.1).getDecimal()*cos(om_a.getRadians())
    incEp_3= SgA(0,0,0.6).getDecimal()*cos((2*om_a.getRadians())+(2*f_a.getRadians())-(2*d_a.getRadians()))
    incEp_4= SgA(0,0,0.1).getDecimal()*cos((2*om_a.getRadians())+(2*f_a.getRadians()))
    incEp= incEp_1 - incEp_2 + incEp_3 + incEp_4

    epsi_m= EPSILON.getDecimal() - (SgA(0,0,4681).getDecimal()*t)
    epsi_ma=DcA(epsi_m)

    incAlfa_1 = cos(epsi_ma.getRadians()) + (sin(epsi_ma.getRadians())*sin(alfa.getRadians())*sin(delta.getRadians()))
    incAlfa_2 = cos(alfa.getRadians())*tan(delta.getRadians())*incEp
    incAlfa = (incAlfa_1 * incOm) - incAlfa_2

    incDelta_1 = sin(epsi_ma.getRadians())*cos(alfa.getRadians())*incOm
    incDelta_2 = sin(alfa.getRadians()) * incEp
    incDelta = incDelta_1 + incDelta_2

    alfa_1=alfa.getDecimal() + incAlfa
    delta_1=delta.getDecimal() + incDelta

    return DcA(alfa_1),DcA(delta_1)

