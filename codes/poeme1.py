# Poème version 1
# http://amienspython.tuxfamily.org/sources/codes/poeme1.py

# Créé par IANTE, le 12/02/2011
from __future__ import division
from lycee import *

poeme=fich2chaine()
CarSpeciaux=['.',',','!',"'","\n",';','?',':']
for c in CarSpeciaux:
    poeme=poeme.replace(c," ")
mots=poeme.split(" ")
for m in mots:
    if m<>"" : print reste(len(m),10),
