#!/usr/bin/env python3
import os
from gestor_notas import GestorNotas

gestor = GestorNotas()
def main():
   while True:
       print("\n---------------Menu---------------\n----------------------------------")
       print("1. Ingresar notas")
       print("2. Leer notas")
       print("3. Buscar nota")
       print("4. Eliminar nota")
       print("5. Salir")
       opcion = int(input("\n[+]Ingrese una opcion: "))
       
       if opcion == 1:
           contenido = input("\n[+]Ingrese el contenido de la nota: ")
           gestor.agregar_nota(contenido)        

       
       elif opcion == 2:
           gestor.leer_notas()
       
       elif opcion == 3:
            texto_buscar = input("\n[+]Ingrese el texto a buscar: ")
            nota = gestor.buscar_nota(texto_buscar)
           
            print(f"\n[+]Nota encontrada: {nota}")   
             
       
       elif opcion == 4:
            texto_a_eliminar = input("\n[+]Ingrese la nota que desea eliminar: ")
            gestor.eliminar_nota(texto_a_eliminar)

       
       elif opcion == 5:
            print("\n[+]Saliendo...")
            break              
       else:
            print("\n[!] La opcion indicada no es correcta ...")
       
       input(f"\n[+]Presiona una tecla para continuar")
       os.system("cls" if os.name == "nt" else "clear")    
       

if __name__ == '__main__':
    main()