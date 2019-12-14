# Recherche d'un couple d'entiers (x,y) solution de ax+by=c
# https://edupython.tuxfamily.org/sources/view.php?code=euclide

# Ce programme fournit une solution particulière de l'équation Diophantienne du programme de la spécialité de TS
a, b, c = demande ("Résolution de ax + by = c dans N.\n Entrez les valeurs entières de a, b et c séparées par une virgule.")
# placer un \n dans le texte crée un retour à la ligne dans le prompteur
d = pgcd (a, b)
if reste (c, d) > 0 :
    print ("Aucune solution, car", d, " divise", a, "et", b,end="")
    print ("mais ne divise pas", c)
else :
    # Initialisations, on laisse invariants p * a0 + q * b0 = a et  r * a0 + s * b0 = b.
    a0, b0, c0 = a/d, b/d, c/d
    p, q, r, s = 1, 0, 0, 1
    while b != 0 :
        res = reste (a, b)                                    # Ordonner a et b est inutile : la boucle s'en charge.
        quot = quotient (a, b)
        a, b = b, res
        p, q, r, s = r, s, p - quot * r, q - quot * s
    print ((p * c0), "*", (a0 * d), "+ (", (q * c0), ") *", (b0 * d), "=", d * c0)
