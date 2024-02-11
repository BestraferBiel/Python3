#!/usr/bin/env python3

import os
import sys



directorio =os.getcwd() # Devuelve el directorio de trabajo actual
print (f"La ruta actual de trabajo es: {directorio}")
archivos = os.listdir(directorio) # Devuelve una lista con los archivos y directorios del directorio actual
print (f"Los archivos y directorios del directorio actual son: {archivos}")


#Usando el modulo sys
print (f"Nombre del escipt: {sys.argv[0]}")
print (f"Numero de argumentos: {len(sys.argv)}")

sys.exit(0) # Termina el programa,si le pasamos un numero diferente de 0, el programa termina con un error

