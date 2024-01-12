#!/usr/bin/env python3

cadena = "Hola Mundo"
print(cadena)
print(type(cadena))

lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))

lista.append(64)
lista.append(7)
lista.append(8)
#print(lista[3])

for i in lista:
    print(i)


print("El tamaño de la lista es:",len(lista))

lista.extend([9, 10, 11, 12, 13, 14, 15])
print(lista)
print("El tamaño de la lista es:",len(lista))
#ordenar lista
lista.sort()
print(lista)
