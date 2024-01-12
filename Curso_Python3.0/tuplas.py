#!/usr/bin/env python3

# Tuplas son parecidas a las listas, pero no se pueden modificar
example = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12)
#a, b, c, d, e, f = example

print(len(example))

numeros_pares = tuple( i for i in example if i % 2 == 0)
print(numeros_pares)
