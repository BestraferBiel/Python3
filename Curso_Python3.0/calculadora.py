#!usr/bin/env python3

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2


entrada = input("Ingrese dos numeros separados por coma: ")
num1, num2 = entrada.split(",")

print (type(num1))#Aqui se puede ver que el split devuelve un string
print (type(num2))

print("Suma: ", Calculadora(int(num1), int(num2)).suma())# Se convierte a int para poder operar con ellos
print("Resta: ", Calculadora(int(num1), int(num2)).resta())
print("Multiplicacion: ", Calculadora(int(num1), int(num2)).multiplicacion())
print("Division: ", Calculadora(int(num1), int(num2)).division())
print("--------------------------------------------------")

#-------------------------Otra forma de hacerlo--------------------------------
#vamos a crear otra calculadora usando @staticmethod

class Calculadora2:
    def __init__(self):
        pass
    
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2
    
    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "No se puede dividir entre 0"

print(Calculadora2.suma(1,2))
print(Calculadora2.resta(100,2))
print(Calculadora2.multiplicacion(8,0))
print(Calculadora2.division(10,0))

#-------------------------Otra forma Clase--------------------------------

class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    @classmethod
    def deportivo(cls, marca):
        return cls(marca,"Deportivo","Rojo")
    @classmethod 
    def sedan(cls, marca):
        return cls(marca,"Sedan","Verde")


    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"


deportivo = print(Automovil.deportivo("Mazda"))
sedan = print(Automovil.sedan("Mazda"))

print("------------------------------------------------------------")

class Estudiantes:
    estudiantes = []
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiantes.estudiantes.append(self)
    @staticmethod
    def es_mayor(edad):
        return edad >= 18
    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor(edad):
            return cls(nombre, edad)
        else:
            print(f"El estudiante {nombre}:No es mayor de edad")
    @staticmethod        
    def mostrar_estudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"Estudiante {i}: {estudiante.nombre}")
    

Estudiantes.crear_estudiante("Juan", 20)
Estudiantes.crear_estudiante("Maria", 17)
Estudiantes.crear_estudiante("Pedro", 18)
Estudiantes.crear_estudiante("Luis", 16)
Estudiantes.crear_estudiante("Ana", 19)
Estudiantes.mostrar_estudiantes()

