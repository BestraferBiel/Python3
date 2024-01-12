#!/usr/bin/env python3


class Vehiculo:
    
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True


class FlotaVehiculos:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
   
    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
             print("Matricula: " + vehiculo.matricula + " Modelo: " + vehiculo.modelo)
    
    def alquilar_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.disponible = False
                print("El vehiculo " + vehiculo.matricula + " ha sido alquilado")
                break
        else:
            print("El vehiculo " + matricula + " no esta disponible para alquilar")
    
    def devolver_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if  vehiculo.matricula == matricula:
                vehiculo.disponible = True
                break
        else:
            print("El vehiculo " + matricula + " ya ha sido devuelto anteriormente")    
       



#if __name__ == "__main__":
            
flota = FlotaVehiculos() 
   
auto1=Vehiculo("G1554","Chevrolet 256")
auto2=Vehiculo("F1445","Ford Fiesta")
auto3=Vehiculo("H1673","Fiat Picanto")
auto4=Vehiculo("M67787","Renault Clio")

flota.agregar_vehiculo(auto1)
flota.agregar_vehiculo(auto2)
flota.agregar_vehiculo(auto3)
flota.agregar_vehiculo(auto4)
flota.mostrar_vehiculos()
flota.alquilar_vehiculo("G1554")
print("[+] Mostrar vehiculos disponibles despues de alquilar")
flota.mostrar_vehiculos()
flota.devolver_vehiculo("G1554")
print("[+] Mostrar vehiculos disponibles despues de devolver")
flota.mostrar_vehiculos()
