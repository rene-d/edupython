# Somme de deux fractions
# https://edupython.tuxfamily.org/sources/view.php?code=fractions

# calcul de la somme exacte de deux fractions
# Le dénominateur commun d est le produit des dénominateurs
# On calcule le numérateur n de la somme
# Puis on simplifie la fraction en utilisant le PGCD
n1, d1 = demande ("Entrez la 1ère fraction en indiquant le numérateur et le dénominateur séparés par une virgule")
n2, d2 = demande ("Entrez la 2ème fraction en indiquant le numérateur et le dénominateur séparés par une virgule")
n, d = n1 * d2 + n2 * d1, d1 * d2
p = pgcd (n, d)
n, d = n / p, d / p
print (n1, "/", d1, "+", n2, "/", d2, "=", n, "/", d)
