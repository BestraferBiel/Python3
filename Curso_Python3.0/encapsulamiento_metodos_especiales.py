#!/usr/bin/env python3


class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 # Atributo privado

    def conducir(self, km):
            if km >= 0:
                self.__kilometraje += km
            else:    
                print("los kilometros deben ser mayores que cero")
    def mostrar_kilometraje(self):
        return self.__kilometraje


coche1 = Coche("Ford", "Fiesta")
coche1.conducir(150)

print(coche1.mostrar_kilometraje())
print(coche1._Coche__kilometraje) # Acceso al atributo privado de la clase usando mangleado

#----------------------------------------------

class Caja:
    def __init__(self, *frutas):
        self.frutas = frutas
    
    def mostrar_frutas(self):
        for fruta in self.frutas:
            print(fruta)
    def __len__(self):# Metodo especial para obtener la longitud de la caja
        return len(self.frutas)

caja1 = Caja("manzana", "pera", "naranja", "platano", "sandia")
caja1.mostrar_frutas()
print(caja1.__len__())

#----------------------------------------------
class Pizza:
    def __init__(self,size, *ingredientes):
        self.ingredientes = ingredientes
        self.size = size

    def descripcion(self):
        print(f"pizza de {self.size} con los siguientes ingredientes:{', '.join(self.ingredientes)}")


pizza1 = Pizza(25, "queso", "tomate", "jamon", "champiñones")

pizza1.descripcion()
        
#----------------------------------------------   
class MIlista:
    def __init__(self, *valores):
        self.valores = valores
    def __getitem__(self, indice):    
        return self.valores[indice]# Metodo especial para acceder a un elemento de la lista

lista1 = MIlista(1,2,3,4,5,6,7,8,9,10)    
print(lista1[5]) # Acceso a un elemento de la lista

#----------------------------------------------

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y) # Metodo especial para sumar dos puntos
    def __str__(self):
        return f"({self.x}, {self.y})"

punto1 = Punto(1,2)
punto2 = Punto(3,4)
print(punto1 + punto2)
