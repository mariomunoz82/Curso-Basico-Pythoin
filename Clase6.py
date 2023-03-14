# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:03:01 2023

@author: MARIO
"""

#TUPLAS!!!
mi_tupla =1,2,3,4,5
print(mi_tupla)

print(mi_tupla[4])
print(mi_tupla[0])

#Operador :
    
print(mi_tupla[2:4])



mi_tupla =1,2,3,4,5,6,7,8,9,10,11,12

print(mi_tupla[::3])
print(mi_tupla[1:11:2])

letras="a","b","c"
letras[0]=1 # lAS tuplas son inmutables no aceptan agregar nuevos elementos
print(letras)

#Condicion que verifica si un elemento pertenece a una tupla
if "d" in letras:
    print("Letra existe")
else:
    print("letras no existe")