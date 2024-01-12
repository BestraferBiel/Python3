#!/usr/bin/env python3


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self):
        print (f' Me llamo {self.nombre} y tengo {self.edad} años')



persona1 = Persona('Miguel', 30)
persona1.saluda()
persona2 = Persona('Pepe', 35)
persona2.saluda()



class Calculadora:
    def __init__(self, numero):
        self.numero = numero
        

    def suma(self, otro_numero):
        self.numero += otro_numero
        return(self.numero)
    
    def suma_doble(self, numero1, numero2):
       return (self.suma(numero1) + self.suma(numero2))
        

calculadora1 = Calculadora(5)
print(calculadora1.suma(10))
print(calculadora1.suma_doble(10, 20))
