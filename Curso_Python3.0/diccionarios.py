#!/usr/bin/env python3

# Diccionarios
# Un diccionario es una estructura de datos que permite almacenar pares de valores, uno siendo la clave y otro el valor asociado a esa clave. Los diccionarios se conocen también como arrays asociativos o tablas hash.

# Los diccionarios se definen entre llaves y los pares de valores se separan con comas. La clave y el valor se separan con dos puntos.
mi_diccionario = {"nombre": "Carlos", "edad": 22, "cursos": ["Python", "Django", "JavaScript"]}

mi_diccionario["profesion"] = "programador"

#Acceder al valor contenido dentro de la lista que a su vez esta dentro del diccionario
print(mi_diccionario["cursos"][1])

print(mi_diccionario["cursos"])
print(mi_diccionario)
#como saber si existe una clave en el diccionario
print("nombre" in mi_diccionario)
