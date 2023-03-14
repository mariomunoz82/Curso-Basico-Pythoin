# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:40:35 2023

@author: MARIO
"""

#COLECCIONES!!! (sets)

letras={"a","b","c"} #Definiendo el set (No acepta valores repetidos)
#agregando elementos al set
letras.add("g")
letras.update(["z","y","x"])
letras.add("A")

# removiendo elementos del SET
letras.discard("A")
letras.discard("A") #No genera error si el elemento no existe
letras.remove("b") #Genera error si el elemento no existe
letras.pop() #remueve un elemento aleatoriamente del set
letras.clear()
print(letras)

print("H" in letras) #Retorna si un elemento o no existe en el set

print(len(letras))#Devueleve numero de elementos en el set

letras2={"z","y","x"}
print(letras|letras2)#uniendo dos sets

restaletras=(letras-letras2)# restando dos sets
print(restaletras)

print(letras&letras2)

a={1,2,3,4,5,6}
b={1,2,3}
print(a>=b)#obtenemos que b es un subconjunto de a

print(b>=a) #Obtenemos que b no es un subconjunto de a




