# Une division avec un nombre arbitraire de décimales
# https://edupython.tuxfamily.org/sources/view.php?code=division

# Affichage d'un quotient avec le nombre de décimales précisées
# On affiche le quotient entier, puis on complète par la virgule
# et les décimales une à une comme si on posait le calcul
n = demande ("Nombre de décimales")
a = demande ("Dividende")
b = demande ("Diviseur")
print (quotient (a, b), ",",end="")
r = reste(a, b)
for i in range (n):
    r = r*10
    q = quotient (r, b)
    print (q, end="")
    r = reste (r,b)
# Vous pouvez améliorer ce programme en espaçant les décimales par groupes de 3
