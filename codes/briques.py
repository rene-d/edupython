# Les briques de Brian
# http://amienspython.tuxfamily.org/sources/codes/briques.py

# Créé par IANTE, le 17/07/2011
from __future__ import division
from lycee import *
def sommefrac(n1,d1,n2,d2):           #La fonction sommefrac renvoie le résultat de
  n,d=n1*d2+n2*d1,d1*d2               #n1/d1+n2/d2 sous forme irréductible
  p=pgcd(n,d)                         #en divisant pas le PGCD
  return quotient(n,p),quotient(d,p)  #On retourne 2 valeurs : le numérateur et le dénominateur

n,d=0,1
for i in range(1,8):
  for j in range(1,i+1):
    for k in range(1,j+1):
      n,d=sommefrac(n,d,j*k,i)        #On fait la somme des fractions
print n,'/',d
