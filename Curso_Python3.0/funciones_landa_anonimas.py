#!/usr/bin/env python3

# Funciones lambda anónimas
mi_funcion = lambda: print("Hola mundo")
mi_funcion()

# Función lambda con parámetros
mi_funcion = lambda x: x ** 2
print(mi_funcion(5))

# Función lambda con varios parámetros

numero = [2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: x ** 2, numero))

print(cuadrados)

#Otra forma de hacerlo de visualidar map y lambda
cuadrados = map(lambda x: x ** 2, numero)
for i in cuadrados:
      print(i)

#usando filter y lambda para filtrar los numeros pares(/)
pares = list(filter(lambda x: x % 2 == 0, numero))

print(f"Los numeros pares son \n{pares}")

#IMportando la libreria functools    
from functools import reduce

#usando reduce y lambda para sumar todos los numeros de la lista
producto = reduce(lambda x, y: x * y, numero)
print(f"El producto de la lista es: {producto}")
    
