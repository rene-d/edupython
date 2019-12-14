# Découpe d'un carré en 3 zones
# https://edupython.tuxfamily.org/sources/view.php?code=montecarlo

# Les zones sont les domaines du plan délimitées par les courbes
# des fonctions carré et racine carrée, à l'intérieur du carré unité,
# dans un repère orthonormal.
# Les aires sont obtenues par la méthode de Monte Carlo.
# On choisit un point au hasard dans le carré unité 10 000 fois
# Et on estime ainsi l'aire de chaque domaine.
a, b, c = 0, 0, 0
for i in range (10000) :
    x, y = random(), random()
    if y > sqrt (x) : a = a + 1
    elif y > x * x : b = b + 1
    else : c = c + 1
print ("On est dans la zone A", a, "fois sur 10 000.")
print ("On est dans la zone B", b, "fois sur 10 000.")
print ("On est dans la zone C", c, "fois sur 10 000.")
print ("Donc les aires respectives des zones A, B et C",end="")
print ("sont estimées à", a / 10000, ",", b / 10000, "et", c / 10000, "unités d'aire.")
