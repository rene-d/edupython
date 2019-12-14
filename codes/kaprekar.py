# Algorithme de Kaprekar
# https://edupython.tuxfamily.org/sources/view.php?code=kaprekar

# Créé par IANTE, le 19/06/2011
from lycee import *
L=range(10000)
for passage in range(1,20):
    L1=[]
    for n in L :
        d=reste(n,10)
        c=reste(quotient(n,10),10)
        b=reste(quotient(n,100),10)
        a=quotient(n,1000)
        a,b,c,d=sorted([a,b,c,d])
        n1=a*1000+b*100+c*10+d
        n2=d*1000+c*100+b*10+a
        n3=n2-n1
        if not n3 in L1 :
            L1.append(n3)
    print ("Passage",passage,":",len(L1),"possibilités",L1)
    L=L1
