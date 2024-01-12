#!/usr/bin/env python3

import re

texto = "En esta cadena se encuentra una palabra mágica,pero es mágica solo una vez o aparece mágica varias veces"

# Buscar la posición de la primera coincidencia
#matches = re.findall("mágica", texto)
#print(matches)

correo = input("Entre el correo a validar:")

def validar_correo(correo):
    patron= "[a-zA-Z0-9._+-]+@[a-zA-Z]+\\.(com|es|org|net)"
    if re.match(patron,correo):
        print("El correo es valido")
    else:
        print("El correo no es valido")


validar_correo(correo)