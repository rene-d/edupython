# Reconnaître un parallélogramme
# https://edupython.tuxfamily.org/sources/view.php?code=para

# Créé par IANTE, le 18/02/2011
from lycee import *
quad=['C',1,2,'O',4,3,'Q',5,0,'P',2,-3]
if quad[4]-quad[1]==quad[7]-quad[10] and quad[5]-quad[2]==quad[8]-quad[11]:
    print( "Le quadrilatère "+quad[0]+quad[3]+quad[6]+quad[9]+" est un parallélogramme.")
else:
    print ("Le quadrilatère "+quad[0]+quad[3]+quad[6]+quad[9]+" n'est pas un parallélogramme.")
