#!/usr/bin/env python3

import threading
import requests
import time

dominios = ['http://www.google.com', 
            'http://www.yahoo.com', 
            'http://www.facebook.com', 
            'http://www.youtube.com',
            'http://www.wikipedia.org',
            'http://www.twitter.com',
            'http://www.amazon.es',
            'http://www.linkedin.com',
            
            
            ]

def Url_dominio(url):
    tiempo_inicial = time.time()
    for url in dominios:
        respuesta = requests.get(url)
        print(f"La web {url} tiene un codigo de estado:{respuesta.status_code}")
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    print(f"[+]El tiempo de ejecucion es de: {tiempo_total}")

#Url_dominio(dominios)

# Crear un hilo
hilo = threading.Thread(target=Url_dominio, args=(dominios,))
hilo.start()
hilo.join()

