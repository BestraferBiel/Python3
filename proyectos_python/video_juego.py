#!/usr/bin/env python3

#Genero
generos = {

        "Super Mario Bros" : "Aventura",
        "The Legend of Zelda" : "Aventura",
        "Pokemon" : "RPG",
        "Final Fantasy" : "RPG",
        "Street Fighter" : "Lucha",
        "Mortal Kombat" : "Lucha",
        "Metal Gear Solid" : "Accion",
        "Grand Theft Auto" : "Accion",
        "FIFA" : "Deportes",
        "NBA" : "Deportes",
        "Need for Speed" : "Carreras",

        }




#Ventas y Stock
ventas_stock = {

        "Super Mario Bros" : (100, 50),
        "The Legend of Zelda" : (50, 25),
        "Pokemon" : (75, 25),
        "Final Fantasy" : (25, 10),
        "Street Fighter" : (50, 25),
        "Mortal Kombat" : (25, 10),
        "Metal Gear Solid" : (50, 25),
        "Grand Theft Auto" : (75, 25),
        "FIFA" : (100, 50),
        "NBA" : (50, 25),
        "Need for Speed" : (25, 6),

        }


#Clientes

clientes = {

       "Super Mario Bros" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "The_legend_of_zelda" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "Pokemon" : ["Juan", "Pedro", "Maria", "Luis", "Ana", "Juana", "Pedra", "Mariana", "Luisa", "Anita"],
       "Final Fantasy" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "Street Fighter" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "Mortal Kombat" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "Metal Gear Solid" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "Grand Theft Auto" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "FIFA" : ["Juan", "Pedro", "Maria", "Luis", "Ana"],
       "NBA" : ["Juan", "Pedro", "Maria", "Luis", "Ana","Juana", "Pedra", "Mariana", "Luisa", "Anita"],
       "Need for Speed" : ["Juan", "Pedro", "Maria", "Luis", "Ana","Juana", "Pedra", "Mariana", "Luisa", "Anita"],




        }


#los juegos que se encuentran en stock son los siguientes

print("Los juegos que se encuentran en stock son los siguientes: \n")
print("\n".join(ventas_stock.keys())) #Voy a usar join para que se vea mejor(el join se usa de esta forma)


#Elegir un juego
mi_juego = input("\nIngrese el nombre del juego: ")

#Validar que el juego exista
while mi_juego not in ventas_stock.keys():
    print("El juego no existe, ingrese nuevamente")
    mi_juego = input("\nIngrese el nombre del juego: ")

#Sumario

print(f"[i] Resumen del juego: {mi_juego}\n")
print(f"\t[+]Genero: {generos[mi_juego]}")
print(f"\t[+]Ventas: {ventas_stock[mi_juego][0]}")
print(f"\t[+]Stock: {ventas_stock[mi_juego][1]}")
print(f"\t[+]Clientes: {', '.join(clientes[mi_juego])}")    #Voy a usar join para que se vea mejor(el join se usa de esta forma) 



#Total de ventas
total_ventas = 0
for juego in ventas_stock.keys():
    total_ventas += ventas_stock[juego][0]
print(f"\nTotal de ventas: {total_ventas}")


#Otra forma de hacerlo usando landa
#total_ventas2 = sum(map(lambda x: x[0], ventas_stock.values())) 
#print(f"\nTotal de ventas: {total_ventas2}")




#probando cosas 

#creando una lista de los juegos que se encuentran en stock
#lista_juegos = list(ventas_stock.keys())
#print(lista_juegos)
#Esto me devuelve una lista con los juegos que se encuentran en stock mayor a 70 unidades
#for juego in ventas_stock.keys():
 #   if ventas_stock[juego][1] > 25 :
 #       print(f"los juegos {juego} tienen mas de 70 unidades en stock")

#else:
#     print("no hay juegos con mas de 70 unidades en stock")    


