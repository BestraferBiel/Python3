#!/usr/bin/env python3  


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar el metodo abstracto")




class Perro(Animal):
    def hablar(self):
        return f"El {self.nombre} dice:Guau!"




class Gato(Animal):
    def hablar(self):
        return f"El {self.nombre} dice:Miau!"


#Ejemplo de polimorfismo
def hacerHablar(animal):
    print(animal.hablar())

gato = Gato("Garfield")
pero = Perro("Pluto")
print(gato.hablar())
print(pero.hablar())

hacerHablar(gato)
hacerHablar(pero)
