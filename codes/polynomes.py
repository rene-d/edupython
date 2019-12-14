# produit de 2 polynômes
# https://edupython.tuxfamily.org/sources/view.php?code=polynomes

# Créé par IANTE, le 21/06/2011
from lycee import *
A=liste_demande('entrez les coefficients de A(x) par ordre des puissances croissantes')
B=liste_demande('entrez les coefficients de B(x) par ordre des puissances croissantes')
DegA,DegB=len(A)-1,len(B)-1
C=[]
for degre in range(DegA+DegB+1) :
    k,coef=0,0
    while k<=degre :
        if k<=DegA and degre-k<=DegB :
            coef=coef+A[k]*B[degre-k]
        k=k+1
    C.append(coef)
print ('('+affiche_poly(A)+')('+affiche_poly(B)+')='+affiche_poly(C))
