# ???
# http://amienspython.tuxfamily.org/sources/codes/double2.py

# Créé par IANTE, le 28/12/2010
from __future__ import division
from lycee import *
mot="Olouglou dit le dindon"
double=""
i=0;
while i <len(mot):
    double=double+mot[i]
    if mot[i].lower() in ("a","e","i","o","u","y") :
        double=double+mot[i]
    i=i+1
print double
