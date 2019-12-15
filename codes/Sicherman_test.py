# ???
# http://amienspython.tuxfamily.org/sources/codes/Sicherman_test.py

# Créé par IANTE, le 31/07/2011
from __future__ import division
from lycee import *
def comptage(D1,D2):
    L=[]
    for j in range(36):
        f1=reste(j,6)
        f2=quotient(j,6)
        L.append(D1[f1]+D1[f2])
    return compte(L,'effectif')

faces=[0]*12
while faces[0]<13 :
    De1=faces[:6]
    De2=faces[6:]
    X,N=comptage(De1,De2)
    if X==[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] and N==[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]:
        print De1,De2
    faces[11]=faces[11]+1
    for i in range(11,6,-1) :
        if faces[i]>faces[i-1]:
            faces[i]=0
            faces[i-1]=faces[i-1]+1
    if faces[6]==13 :
        faces[6]=0
        faces[5]=faces[5]+1
    for i in range(5,0,-1) :
        if faces[i]>faces[i-1]:
            faces[i]=0
            faces[i-1]=faces[i-1]+1
