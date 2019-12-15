# Nombre de voyelles
# http://amienspython.tuxfamily.org/sources/codes/voyelles.py

# Créé par IANTE, le 28/12/2010
from __future__ import division
from lycee import *
mot="anticonstitutionnellement"
nb=0;i=0;
while i <len(mot):
    if mot[i] in ("a","e","i","o","u","y") :
        nb=nb+1
    i=i+1
print mot,"a",nb,"voyelle(s)."
