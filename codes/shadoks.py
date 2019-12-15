# Compter en Shadoks
# http://amienspython.tuxfamily.org/sources/codes/shadoks.py

# Créé par IANTE, le 29/12/2010
from __future__ import division
from lycee import *
nbS="MEU GA GA BU MEU ZO ZO"
print nbS,"=",
nbS=nbS.replace("GA","0")
nbS=nbS.replace("BU","1")
nbS=nbS.replace("ZO","2")
nbS=nbS.replace("MEU","3")
nbS=nbS.replace(" ","")
d=1;r=0
for i in range(len(nbS),0,-1):
    r=r+eval(nbS[i-1])*d
    d=d*4
print r
