#!/usr/bin/env python3


class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
    def describir(self):
         raise NotImplementedError("Subclase debe implementar el metodo abstracto")

class Auto(Automovil):
    def describir(self):
        return("El modelo es {}, la marca es {} y el color es {}".format(self.modelo, self.marca, self.color))

class Moto(Automovil):
    def describir(self):
        return("El modelo es {}, la marca es {} y el color es {}".format(self.modelo, self.marca, self.color))



auto = Auto("A4", "Audi", "Rojo")
moto = Moto("CBR", "Honda", "Verde")
print(auto.describir())
print(moto.describir())

# Otro ejemplo usando herencia y polimorfismo

class A:
    def __init__(self, x):
        self.x = x
        print(f"El valor de X: {self.x}")

class B(A):
    def __init__(self, x, y):
        super().__init__(x)# Llamamos al constructor de la clase padre y le pasamos el parametro x 
        self.y = y# Inicializamos el parametro y
        print(f"El valor de Y: {self.y}")# Imprimimos el valor de y

b = B(10, 20)# Instanciamos la clase B y le pasamos los parametros x,y, por lo tanto se ejecuta el constructor de la clase B        

