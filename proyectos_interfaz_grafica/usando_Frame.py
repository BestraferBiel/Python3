#!/usr/bin/env python3

import tkinter as tk

ventana = tk.Tk()
ventana.title("Usando Frame")

# Crear un frame
frame = tk.Frame(ventana, bg="blue", bd=5)
label1 = tk.Label(frame, text="Gabriel Cabrera",bg="red")
label2= tk.Label(frame, text="Entrar Datos",bg="yellow")

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)

ventana.geometry("400x300")
ventana.mainloop()

