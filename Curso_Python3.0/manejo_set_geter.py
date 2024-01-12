#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
    
    @property
    def edad(self):
         return self._edad
    
    @edad.setter
    def edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:    
            raise ValueError("Edad no puede ser negativa")


p1 = Persona("Juan", 20)

#p1.edad = -10#seter
print(p1.edad)#geter
#---------------------------------------------

import time

def cronometro(func):#puedo poner tambien *args y **kwargs y funcionaria igual
    def envoltura(num):
        t_inicial = time.time()
        func(num)
        t_final = time.time()
        print(f"El tiempo total de la funcion {func.__name__} es {t_final - t_inicial}")
    return envoltura    



@cronometro
def pausa_corta(num):#puedo poner tambien *args y **kwargs y funcionaria igual
    time.sleep(num)
@cronometro
def pausa_larga(num):#puedo poner tambien *args y **kwargs y funcionaria igual
    time.sleep(num)

pausa_corta(1)
pausa_larga(3)


#---------------------------------------------


#Ejemplo de como usar *args y **kwargs
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total


print(suma(1,2,3,4,5,6,7,8,9,10))


#---------------------------------------------
#Ejemplo de como usar **kwargs
def Presentacion(**kwargs):
    for key, value in kwargs.items():
         print(f"{key} : {value}")


Presentacion(nombre="Juan", edad=20, pais="Mexico", telefono=1234567890)




