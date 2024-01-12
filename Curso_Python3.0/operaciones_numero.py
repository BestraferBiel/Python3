#!/usr/bin/env python3

firts_nomber = 61
second_number = 83
result = firts_nomber ** second_number
print("{:,}".format(result).replace(',','.'))

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,2,3,4,5,6,7,8,9,10]

result2 = lista + lista2
print(result2)

resul2 = list(map(sum,zip(lista,lista2)))
print(list(resul2))
