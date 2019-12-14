# Suite de Fibonacci
# https://edupython.tuxfamily.org/sources/view.php?code=fibonacci

from lycee import *
def fibo(n):
    if n==0 or n==1:
        return 1                     
    else:
        return fibo(n-1)+fibo(n-2)    
		
r=demande("Indice du terme de la suite de Fibonacci?")
print (fibo(r))
