# Poème version 2
# https://edupython.tuxfamily.org/sources/view.php?code=poeme2

# Créé par IANTE, le 12/02/2011
from lycee import *
poeme=fich2chaine()
NbDecimales,pos=0,0
reponse=""
while pos<len(poeme):
    NbLettres=0
    while pos<len(poeme) and not poeme[pos]in ('.', ',', '!', "'", "\n", ';', '?', ':', ' '):
        NbLettres=NbLettres+1
        pos=pos+1
    reponse=reponse+str(reste(NbLettres,10))
    NbDecimales=NbDecimales+1
    if NbDecimales==1 : reponse=reponse+","
    while pos<len(poeme) and poeme[pos]in ('.',',','!',"'","\n",';','?',':',' '):
        pos=pos+1
print (reponse)
