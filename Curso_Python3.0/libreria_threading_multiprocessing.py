#!/usr/bin/env python3

import threading
import multiprocessing
import time

def tarea(num_tarea):
    print(f"[+]Inicio de la tarea {num_tarea}")
    time.sleep(2)
    print(f"[-]Fin de la tarea {num_tarea}\n")

#se crea el hilo siempre con la clase Thread y se le pasa como argumento la función tarea y los argumentos de la función tarea
thead1=threading.Thread(target=tarea, args=(1,))
thead2=threading.Thread(target=tarea, args=(4,))

#se inicia el hilo
thead1.start()
thead2.start()
#se espera a que termine el hilo en paralalelo

thead1.join()
thead2.join()
print("Fin de la ejecución")

#usando multiprocessing
#se crea el proceso siempre con la clase Process y se le pasa como argumento la función tarea y los argumentos de la función tarea
p1=multiprocessing.Process(target=tarea, args=(1,))
p2=multiprocessing.Process(target=tarea, args=(4,))
#se inicia el proceso
p1.start()
p2.start()
#se espera a que termine el proceso en paralalelo
p1.join()
p2.join()
print("Fin de la ejecución usando procesos")