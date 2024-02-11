#!/usr/bin/env python3

import tkinter as tk
from  SimpleTextEditor import SimpleTextEditor


ventana = tk.Tk()
ventana.title("Bloc de Notas")
#voy a crear una instancia de una calse 
editor = SimpleTextEditor(ventana)


#creando el menu
barra_menu = tk.Menu(ventana)

#creando los elementos del menu o las opciones del menu (Archivo)
menu1 = tk.Menu(barra_menu, tearoff=0)
menu1.add_command(label="Nuevo", command=editor.nuevo_archivo)
menu1.add_command(label="Abrir", command=editor.abrir_archivo)
menu1.add_command(label="Guardar", command=editor.guardar_archivo)
menu1.add_command(label="Salir", command=editor.salir)

#creando los elementos del menu o las opciones del menu (Edicion)
menu2 = tk.Menu(barra_menu, tearoff=0)
menu2.add_command(label="Copiar")
menu2.add_command(label="Cortar")
menu2.add_command(label="Pegar")

#creando los elementos del menu o las opciones del menu (Ayuda)
menu3 = tk.Menu(barra_menu, tearoff=0)
menu3.add_command(label="Licencia", command=editor.mostrar_licencia)


#cascada de menu
barra_menu.add_cascade(label="Archivo", menu=menu1)
barra_menu.add_cascade(label="Edicion", menu=menu2)
barra_menu.add_cascade(label="Ayuda", menu=menu3)

#agregando el menu a la ventana,esto hace que se muestre
ventana.config(menu=barra_menu)



#creando el cuadro de texto o la caja de texto
ventana.geometry("700x400")
ventana.mainloop()

