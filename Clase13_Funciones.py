# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:31:29 2023

@author: MARIO
"""

####### Funciones#########

# Definiendo una funcion
def saludo(nombre):
    print("Hola",nombre)
saludo("Adam")

def suma(a,b):
    print(a+b)
suma(10,5)

#Por defecto elvalor de los parametros se asignan por el orden
# si quiere cambiarse hay que indicarlo al momento de llamar la funcion

def suma(a,b):
    print(a/b)
suma(b=10,a=5)

# al colocar el * permite agregar multiples vallores como argumento a una funcion

def suma(*numeros):
    for x in numeros:
        print(x)
suma(1,2,3,4,5)

#Al asignar doble ** quiere decir que se va a asignar un diccionario

def suma(**numeros):
    for x,y in numeros.items():
        print(x,y)
dic={"a":1,"b":2,"c":3}
suma(**dic)

""" breve reseña de lo que hara la funcion """
def saludo(nombre):
    print("Hola",nombre)
    return "Bienvenido a Python"
    print("Adios",nombre)
print(saludo("Adam"))



lista1=[]
lista2=[]
lista3=[]

def obtenerresultado(a,b):
    if a> b:
        try:
            divisor=a/b
            lista1.append(divisor) 
        except ZeroDivisionError:
            print("La suma entre 0 no es posible")        
    elif a<b:
            suma=a+b
            lista2.append(suma)
    else:
        producto=a*b
        lista3.append(producto)
        
for i in range(1,4):
    obtenerresultado(i+1,i+2)   
    
print(lista1)
print(lista2)
print(lista3)

#Otro comentario en archivo 13


        
    

