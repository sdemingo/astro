#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

Script para scrappear la página de efemerides del Observatorio
Astronómico Nacioan (OAN) y obtener en formato orgmode los próximos
eventos astronómicos vistos desde una localización.

   Sergio de Mingo Gil
'''

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import string
import time
import datetime
import requests
from bs4 import BeautifulSoup


def orgmodeFile(events,filename):
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
    s="#+TITLE:Próximos eventos astronómicos\n\n"
    s+="Generado en "+st+" desde http://www.oan.es/servidorEfem/index.php\n\n"
    s+="* Próximas efemérides\t\t\t:astro:\n"
    for e in events:
        s+= "** "+e["title"]+"\n"
        s+= "\t<"+e["timestamp"]+">\n"
        s+= "\t"+e["desc"]+"\n\n"

    print s

def parseTimeStamp(srcTime):
    timetext = re.search("(\d{4}\-\d{2}\-\d{2} \d{2}:\d{2})", srcTime)
    return timetext.group(1)


def getTitle(desc):
    title=re.search("([\w\- ]+)",desc,re.UNICODE)
    if title:
        return title.group(1)
    else:
        return desc

def main():

    s = requests.Session()
    payload={
        "locName":"loc/-3.86514/40.3317",    # Localización
    }
    r = s.post("http://www.oan.es/servidorEfem/index.php", data=payload)
    soup = BeautifulSoup(r.text,"lxml")

    a= soup.find_all("a",{"name":"nextEvents"})
    table= a[0].find_next_sibling("table")

    events=[]
    for row in table.find_all("tr"):
        desc=row.findNext("td").findNext("a").string
        title=getTitle(desc)
        rawstamp=desc.findNext("td").findNext("font").string
        timestamp=parseTimeStamp(rawstamp)
        events.append({"desc":desc,"rawstamp":rawstamp,"timestamp":timestamp,"title":title})
        
    # org mode out
    orgmodeFile(events,"")


if (__name__=='__main__'):
    main()
