# Vendredi 13
# http://amienspython.tuxfamily.org/sources/codes/vendredi.py

from __future__ import division
from lycee import *
jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
mois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
nbjours=[31,28,31,30,31,30,31,31,30,31,30,31]
for jan in range(7):
    print "Si le 13 Janvier est un",jours[jan]," : ",
    m=0;j=jan;
    while reste(j,7)<>4 and m<12:
        j=j+nbjours[m]
        m=m+1;
    if reste(j,7)==4:
        print "Le 13",mois[m],"sera un Vendredi 13"
    else :
        print "il n'y a pas de Vendredi 13"
