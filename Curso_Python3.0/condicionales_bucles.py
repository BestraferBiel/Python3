#/usr/bin/env python3

# Condicionales
# if, elif, else

name = ['Juan', 'Pedro', 'Luis', 'Maria', 'Ana']

for i in name:
    print(f"El nombre para esta vuelta es {i}")
    if i == 'Maria':
        print(f"El nombre es {i} se encuentra en la posicion {name.index(i)}")
        break
#    else:
 #       print(f"El nombre es {i} se encuentra en la posicion {name.index(i)}")

# Bucles
a = 0
while a < 5:
    print(a)
    a += 1
#Devolver el indice de un elemento en una lista    
for i,n in enumerate(name):
    print(i,n)
#Diccionarios
frutas = {'manzana': 1, 'pera': 2, 'naranja': 3, 'limon': 4, 'mango': 5}
for i in frutas:
    print(f"La fruta {i},tiene un valor de {frutas[i]}")

for i in frutas.items():
    print(f"La fruta {i[0]},tiene un valor de {i[1]}")


#Bucles anidados
my_list = [[11,112,113,114,2235],[26,27,28,29,210],[11,12,13,14,15]]
print(my_list[2][0])#esto es para acceder a un elemento de la lista
for i in my_list:
    print(i)
    for j in i:
        print(j) #esto es para acceder a cada elemento de la lista
#List comprehension
#lista de comprension
lista_numero = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrado = [i ** 2 for i in lista_numero]
print(lista_cuadrado)
