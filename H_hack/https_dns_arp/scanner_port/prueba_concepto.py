#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor#para que sea mas rapido el escaneo y maneja la cantidad de hilos que se van a ejecutar

def imprimir (x,y):
    print(x)
    print(y)

my_list = [1,2,3,4,5]
y=2
with ThreadPoolExecutor() as executor:
      #executor.submit(imprimir, my_list,my_list)
      executor.map(lambda x: imprimir(x, y), my_list)