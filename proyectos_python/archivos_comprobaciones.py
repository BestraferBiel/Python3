#!/usr/bin/env python3

import os

if os.path.exists("proyectos_python/archivo.txt"):
    print("[+]El archivo existe")
else :
    print("[+]El archivo no existe")


ruta = os.path.join("proyectos_python","archivo.txt")
print("[+]La ruta absoluta es: ", ruta)

print("[+]El nombre del archivo es: ", os.path.basename(ruta))

print("[+]El directorio del archivo es: ", os.path.dirname(ruta))

directorio = os.path.split(ruta)
print("[+]El directorio y el archivo son: ", directorio)