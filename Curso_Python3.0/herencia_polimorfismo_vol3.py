#!/usr/bin/env python3


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def saludar(self):
        # super().saludar()
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años con un sueldo {self.sueldo}")




persona1 = Persona("Juan", 28)
persona1.saludar()

empleado1 = Empleado("Karla", 30, 5000)     
empleado1.saludar()
