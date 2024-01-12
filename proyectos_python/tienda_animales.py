#!/usr/bin/env python3

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def __str__(self) :
        return f"[+]{self.nombre} ({self.especie}) -> {'Alimentado' if self.alimentado else 'Hambriento'}"#se usa para hacer una condicion en una sola linea
    def alimentar(self):
        self.alimentado = True

class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []
    
    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)        
    
    def alimentar_animales(self):
        for animal in self.animales:
         animal.alimentar()
    
    def vender_animal(self, nombre):
         for animal in self.animales:
             if animal.nombre == nombre:
                 animal.alimentado = False
                 self.animales.remove(animal)
                 print(f"[+]Se vendio a {animal.nombre}")
                 return 
         print(f"[-]No se encontro a {nombre} en la tienda")   

if __name__ == "__main__":

    tienda = TiendaAnimales("Mi tienda de animales")


    gato = Animal("Tijuana", "Gato")
    perro = Animal("Rocky", "Perro")
    pez = Animal("Nemo", "Pez") 


    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    tienda.agregar_animal(pez)
    tienda.mostrar_animales()
    tienda.alimentar_animales()
    print("[+]Animales alimentados")
    tienda.mostrar_animales()
    tienda.vender_animal("Rocky444")
    print("[+]Animales que quedan en la tienda dsp de vender ")
    tienda.mostrar_animales()


