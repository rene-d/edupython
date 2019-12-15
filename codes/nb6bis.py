# Compter le nombre de 6
# http://amienspython.tuxfamily.org/sources/codes/nb6bis.py

from __future__ import division
from lycee import *
De=[]
for i in range(1000) :
    De.append(randint(1,6))
n=De.count(6)
print De
print 'Sur 1 000 lancers, vous avez obtenus',n,'fois le chiffre 6.'
if n>0 :
    print 'Le premier 6 a été obtenu au tirage numéro',De.index(6)+1
