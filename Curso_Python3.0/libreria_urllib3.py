#!/usr/bin/env python3 

import urllib3

http = urllib3.PoolManager()# controlador de conexiones
response = http.request('GET', "https://httpbin.org/get")# peticion GET

#print(response.data.decode())# decodificamos la respuesta


#otra peticion POST
response = http.request('POST', "https://httpbin.org/post", fields={'nombre': 'Juan', 'apellido': 'Perez'})
print(response.data.decode())# decodificamos la respuesta