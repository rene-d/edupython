# Coefficient de Gini
# https://edupython.tuxfamily.org/sources/view.php?code=gini

# Créé par AgneS, le 04/09/2011
from lycee import *
listedeciles=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
proportions=[0.03,0.045,0.055,0.067,0.079,0.092,0.107,0.125,0.152,0.248]
listedeciles,cumul=ECC(listedeciles,proportions)
polygoneECC(listedeciles,proportions)
repere.plot([0,1],[0,1])
somme=0
for i in range (9):
    somme=somme+0.1*cumul[i]
somme=somme+0.05*cumul[9]
gini=1-2*somme
print ("Le coefficient de Gini vaut",gini, ".")
repere.show()
