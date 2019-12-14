# Somme des carrés des 100 premiers entiers
# https://edupython.tuxfamily.org/sources/view.php?code=sommecarre

# Créé par AgneS, le 17/06/2013 en Python 3.2

# On calcule la somme 1² + 2² + 3² + ... + 100²

total=0
for n in range(101):            # n prend toutes les valeurs entières de 1 à 100
  total=total+n*n
  if n<100:                    # Test afin d'adapter l'affichage à la valeur de n
                            # dans une boucle dont on connaît le nombre de répétitions.
      print (n,"² + ", end="")
  else :
      print (n,"² = ", end="")
print (total)
