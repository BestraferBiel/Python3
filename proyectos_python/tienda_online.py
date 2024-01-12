#!/usr/bin/env python3

#Tienda online
class Producto:
    productos = []
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.productos.append(self)

    #@staticmethod
    def convertir_a_euros(self):
        return self.precio * 0.90605 # 1 dolar = 0.90605 euros
    
    @classmethod
    def calcular_total(cls):
        total = 0
        for producto in cls.productos:
            total += producto.precio
        return total
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.nombre, producto.precio)
    @classmethod        
    def mostrar_productos_precio_euros(cls):
       for producto in cls.productos:
           print(producto.nombre, producto.convertir_a_euros())
  

producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalon", 50)
producto3 = Producto("Calcetines", 10)
producto4 = Producto("Zapatos", 80)
    
print("El precio de la camiseta en € es:",Producto.convertir_a_euros(producto1))

print("El precio total de los productos en dolares es:",Producto.calcular_total())
Producto.mostrar_productos(Producto)
Producto.mostrar_productos_precio_euros()
