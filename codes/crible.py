# Crible d'Ératosthène
# https://edupython.tuxfamily.org/sources/view.php?code=crible

# Initialise la variable i
liste = list(range (2, N))       # Crée la liste des nombres entiers de 2 à N

while indice < len (liste) :
                           # On utilise la longueur de la liste pour compter
                           # les éléments qui la constituent.
    nombre = liste[indice]
    n = 2                  # Après avoir initialisé le multiplicateur,
                           # on calcule les multiples de chaque nombre choisi
                           # et on les élimine de la liste
                           # si ils y sont encore.
    while n * nombre < N :
        multiple = n * nombre
        if multiple in liste :
            liste.remove(multiple)
        n = n + 1
    indice = indice + 1    # passe au nombre suivant dans la liste
print (liste)
