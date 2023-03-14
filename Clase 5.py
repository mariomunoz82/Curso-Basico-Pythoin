# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:45:29 2023

@author: MARIO
"""

numeros=[1,2,3,4,5]
print(numeros)

lista=["a",3,5.5,True,"Hoy es 11 de Febrero"]
print(lista)

nombre="Python"
lista=list(nombre)
print(lista)

milista=[]
print(milista)

#La funcion list tiene que ser con un iterable si no no funciona
numeros="2500"
lista=list(numeros)
print(lista)

mi_lista = ["una","dos","tres","cuatro","cinco","seis"]
mi_lista.append("cuatro")
mi_lista.append(5)
print(mi_lista)

#metodo index
print(mi_lista.index("dos"))

mi_lista.insert(3,8.5)
print(mi_lista)

print(mi_lista[-4])

mi_lista[5]="siete"
print(mi_lista)


print(len(mi_lista))
list.clear(mi_lista)
print(mi_lista)


lista=[1,2,3]
c=lista*3
print(lista)
print(c)

lista.reverse()
print(lista)


print(min(lista))

Lista2=[10,14,55,3,8,9,100]
print(Lista2)
Lista2.sort()
print(Lista2)
Lista2.sort(reverse=True)
print(Lista2)