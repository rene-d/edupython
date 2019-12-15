# Suite de Fibonacci
# http://amienspython.tuxfamily.org/sources/codes/fibonacci.py

from __future__ import division
from lycee import *
def fibo(n):
    if n==0 or n==1:
        return 1                       #U0=U1=1
    else:
        return fibo(n-1)+fibo(n-2)     #Un=Un-1+Un-2
r=demande("Indice du terme de la suite de Fibonacci?")
print fibo(r)
