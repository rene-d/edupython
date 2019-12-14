# Compter le nombre de 6
# https://edupython.tuxfamily.org/sources/view.php?code=nb6bis

from lycee import *
De=[]
for i in range(1000) :
    De.append(randint(1,6))
n=De.count(6)
print (De)
print ('Sur 1 000 lancers, vous avez obtenus',n,'fois le chiffre 6.')
if n>0 :
    print ('Le premier 6 a été obtenu au tirage numéro',De.index(6)+1)
