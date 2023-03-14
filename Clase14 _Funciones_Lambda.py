# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:09:49 2023

@author: MARIO
"""

resultado=lambda x: x**2
print(resultado(5))


resultado=lambda x: True if x**2 >=10 else False
print(resultado(3))


def f(x,y,z=2):
    return(x+y)*z
print(f(3,2))

f=lambda x,y,z=2: (x+y)*z
print(f(3,2))

numeros=[-4,5,6,8,0,-3,-7,-9]
#Filter es una funcion que nos permite crear una lista a partir de los valores
# que arrojan una condicion verdadera
x=filter(lambda x: x>0, numeros)
print(list(x))



