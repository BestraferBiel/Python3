#!/usr/bin/env python3

import tkinter as tk

def accion_boton():
    print("Se ha pulsado el botón")
    label_muestra.config(text="Se ha pulsado el botón")


ventana = tk.Tk()
ventana.title("Mi primera app")
# Crear un label (etiqueta)
texto_info = "[+]Hola, esto es un label[+]"
label1 = tk.Label(ventana, text=texto_info, bg="blue", fg="white", font=("Arial", 12))
label_muestra = tk.Label(ventana, text="", bg="green", fg="white", font=("Arial", 12))
boton = tk.Button(ventana, text="Click aquí", bg="red",command=accion_boton ,fg="white", font=("Arial", 12))
# Empaquetar el label (etiqueta) usando pack()
#label1.pack(fill=tk.X)
#label_muestra.pack()
#boton.pack(side=tk.BOTTOM)
#-------------------------------------------
#Usando grid
#label1.grid(row=0, column=0)
#label_muestra.grid(row=1, column=0)
#boton.grid(row=2, column=0)
#-------------------------------------------
#Usando place
label1.place(x=0, y=0)
label_muestra.place(relx=0.8, rely=0.3)
boton.place(x=0, y=60)
#-------------------------------------------
ventana.geometry("500x400")
ventana.mainloop()
