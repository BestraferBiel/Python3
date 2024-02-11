#!/usr/bin/env python3
import requests

ruta_especifica = "D:\Python3\Curso_Python3.0\index.html"
# Usando el modulo requests
url = "https://www.google.es"
respuesta = requests.get(url)
print("El codigo de estado es: ",respuesta.status_code)
with open(ruta_especifica,"wb") as archivo:#guardamos el contenido de la pagina en un archivo
    archivo.write(respuesta.content)


#Usando post

payload = {"username":"admin","password":"1234"}
heders = {"User-Agent":"my-app/0.0.1"}
respuesta = requests.post("https://httpbin.org/post",data=payload,headers=heders)
print(respuesta.content)


#otro ejemplo

response = requests.get("https://httpbin.org/get")
data = response.json()
if "headers" in data and "User-Agent" in data["headers"]:
 user_agent = data["headers"]["User-Agent"]
 print("User-Agent: ",user_agent)
else:
    print("No se encontro el header User-Agent")

