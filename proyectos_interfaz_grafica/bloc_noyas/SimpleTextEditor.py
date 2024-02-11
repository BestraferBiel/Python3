#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext

class SimpleTextEditor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.texto_area = tk.Text(self.ventana)
        self.texto_area.pack(fill="both", expand=1)
        
    def salir(self):
         respuesta = messagebox.askyesno("Salir", "Esta seguro que desea salir")
         if respuesta:
             self.ventana.destroy()
   
    def guardar_archivo(self):
         archivo = filedialog.asksaveasfile(title="Guardar Archivo", mode="w", defaultextension=".txt")
         if archivo is not None:
              contenido = self.texto_area.get(1.0, tk.END)
              archivo.write(contenido)
              archivo.close()
              self.texto_area.delete(1.0, tk.END)

    def abrir_archivo(self):
         self.texto_area.delete(1.0, tk.END)
         archivo = filedialog.askopenfile(title="Abrir Archivo", mode="r", defaultextension=".txt")
         if archivo is not None:
              contenido = archivo.read()
              self.texto_area.insert(tk.END, contenido)
              archivo.close()              
    
    def nuevo_archivo(self):
            respuesta = messagebox.askyesno("Nuevo", "Esta seguro que desea crear un nuevo archivo")
            if respuesta:
                self.texto_area.delete(1.0, tk.END)
    
    def mostrar_licencia(self):
         ventana_licencia = tk.Toplevel(self.ventana)
         ventana_licencia.title("Licencia")

         texto_licencia = """
         Licencia del Bloc de Notas

         1. Este software es gratuito y de código abierto.
         2. Puedes usar, modificar y distribuir este software de acuerdo con los términos de la licencia.
         3. No hay garantía. El software se proporciona "tal cual" sin garantía de ningún tipo.

         (c) 2022 Python Software Foundation.Creado por : Gabriel Cabrera Romo
           """

         text_widget = scrolledtext.ScrolledText(ventana_licencia, wrap=tk.WORD, width=70, height=30, font=("Arial", 10))
         text_widget.insert(tk.END, texto_licencia)
         text_widget.configure(state="disabled")
         text_widget.pack(padx=10, pady=10)
         text_widget.tag_configure("center", justify="center")
         text_widget.tag_add("center", 1.0, "end")

        