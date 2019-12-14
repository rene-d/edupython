# Elections
# https://edupython.tuxfamily.org/sources/view.php?code=elections

# Créé par IANTE, le 27/08/2011
from lycee import *
p,a,b=0,-1,-1
for k in range(101):
    p=p+binomial(100,k)*puissance(0.52,k)*puissance(0.48,100-k)
    if a==-1 and p>0.025 :
        a=k
    if b==-1 and p>=0.975 :
        b=k
print ("On peut considérer l'affirmation de monsieur Z exacte ", end="")
print("au seuil de 5%, si le nombre de personne ayant répondu ", end="")
print("positivement est dans l'intervalle [",a,";",b,"].")
