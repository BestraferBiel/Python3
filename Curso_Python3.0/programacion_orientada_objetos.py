#!/usr/bin/env python3

# Clase: Programación Orientada a Objetos

# Definición de la clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print (f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años") 

# Instanciación de la clase

persona1 = Persona("Juan", 25)
persona2 = Persona("Carlos", 30)
Persona.saludar(persona1)
Persona.saludar(persona2)

#----------------------------------------------------------------------------------------------

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def description(self):
        print (f"Soy un animal llamdo {self.nombre} y mi raza es  {self.tipo} ")


# Instanciación de la clase

animal1 = Animal("Tijuana", "gato")
animal2 = Animal("ChuChu", "perro")
animal3 = Animal("Piolin", "pajaro")

Animal.description(animal1)
Animal.description(animal2)
Animal.description(animal3)# Se puede llamar de esta manera tambien,es la mas comun...
animal1.description()# Se puede llamar de esta manera tambien...

#----------------------------------------------------------------------------------------------

class Cuenta_Bancaria:
    lista_cuentas = [] # Se crea una lista vacia para almacenar las cuentas que se vayan creando
    def __init__(self, cuenta, nombre, dinero = 0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero
        Cuenta_Bancaria.lista_cuentas.append(self)# Se agrega a la lista de cuentas la cuenta que se esta creando
    
    def depositar(self, dinero):
        self.dinero += dinero
        print(f"Se han depositado {dinero} € la cuenta {self.cuenta} de {self.nombre}")
    
    def retirar(self, dinero):   
        if self.dinero >= dinero:
            self.dinero -= dinero
            print(f"Se han retirado {dinero} € de la cuenta {self.cuenta} de {self.nombre}")
        else:
            print(f"No hay suficiente dinero en la cuenta {self.cuenta} de {self.nombre} para retirar {dinero} €")
    
    @classmethod # Esto se usa para llamar a un metodo de la clase y no de la instancia
    def listaCuentas(cls):
         for usuario in cls.lista_cuentas:
             print(f"Cuenta: {usuario.cuenta}, Nombre: {usuario.nombre}, Dinero: {usuario.dinero}")


        


mi_cuenta = Cuenta_Bancaria("123456789", "Juan", 1000)
mi_cuenta.depositar(500)
mi_cuenta.retirar(100)
print(mi_cuenta.dinero)
    

mi_cuenta2 = Cuenta_Bancaria("123456789", "Carlos", 3000000)
mi_cuenta2.depositar(500)
mi_cuenta2.retirar(100000000000000)
print(mi_cuenta2.dinero)
 
print("-------------------------")
Cuenta_Bancaria.listaCuentas()



#----------------------------------------------------------------------------------------------
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    @property # Esto se usa para que se pueda acceder a los atributos como si fueran metodos sin tener que poner los parentesis ala hora de llamarlos
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * self.base + 2 * self.altura
    
    def __str__(self):# Este metodo se usa para que cuando se imprima el objeto se muestre lo que se quiera
        return f"Rectangulo de base {self.base} y altura {self.altura}"


    def cambiar_tamanno(self, escala):
        self.base = self.base * escala
        self.altura = self.altura * escala

mi_rectangulo = Rectangulo(10, 20)
print(mi_rectangulo.area)# Se puede acceder a los atributos como si fueran metodos sin tener que poner los parentesis ala hora de llamarlos por el uso de @property
print(mi_rectangulo.perimetro())
mi_rectangulo.cambiar_tamanno(2)
print(mi_rectangulo)


#----------------------------------------------------------------------------------------------

class libro:
    IVA = 0.21
    limite_betseller = 500
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    
    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}"
    
    @staticmethod
    def es_best_seller(ventas):# Como  agregue @staticmethod no hace falta poner self de lo contrario seria self,ventas
        return ventas > libro.limite_betseller
    @staticmethod
    def precio_con_impuesto(precio):
        return precio + precio * libro.IVA 

mi_libro = libro("El señor de los anillos", "J.R.R Tolkien", 12.99)
print(mi_libro)
print(libro.es_best_seller(10000))# Como  agregue @staticmethod no hace falta poner la instancia solo libro.es_best_seller
print(libro.precio_con_impuesto(mi_libro.precio))# Como  agregue @staticmethod no hace falta poner la instancia solo libro.es_best_seller






