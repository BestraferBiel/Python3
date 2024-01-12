#!/usr/bin/env python3


# Función para abrir un archivo

f = open('prueba.txt', 'w')

f.write('Probando usando python\n')


f.close()

# Otra forma de abrir un archivo

with open('prueba2.txt', 'w') as f:
    f.write('Probando usando python\n')
    f.write('Segunda linea\n')
    f.write('Tercera linea\n')


# Leer un archivo

with open('/etc/hosts', 'r') as f:#esta funcion tambien es iterable lo que significa que podemos usar un for para recorrerlo

    for linea in f:
        print(linea.strip())#strip elimina los espacios en blanco al inicio y al final de la linea

#colocar una lista en un archivo

lista = ['Pedro\n', 'Robeto\n', 'Gabriel\n', 'Juan\n']

with open('lista.txt', 'w') as f:
    f.writelines(lista)
