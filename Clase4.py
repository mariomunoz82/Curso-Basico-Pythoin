# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:12:47 2023

@author: MARIO
"""

a=5
if a>3:
    print("El numero es mayor a 3")
    

numero=int(input("Ingrese un numero"))
if numero<0:
    print("Solo se permiten numeros positivos")
else:
    print("El numero es mayor a 0")
    

a=3
b=3
if a==b:
    print("Los numeros son iguales")
else:
    print("Los numeros no son iguales")
    

x=int(input("Ingrese un numero"))
if x >5:
    print("El numero es mayor a 5")
elif x==0:
    print("El numero es cero")
elif x==1:
    print("El numero es 1")
else:
    print("El numero es negativo")
    

edad=int(input("Ingrese su edad"))
if edad>18 and edad < 70:
    print("Puedes ingresar")
elif edad >70:
    print("no puedes ingresar, persona de tercera edad")
else:
    print("No puedes ingresar")
    

password=input("Ingrese su contraseña")
if len(password)>=8:
    print("Contraseña es demasiado larga")
    if password== "MiClaveSegura":
        print("La contraseña es correcta")
    else:
        print("la contraseña es incorrecta")
else:
    print("la contraseña es demasiado corta")
    if password!="MiClaveSegura":
        print("La contraseña es incorrecta")
    
    

