#!/usr/bin/env python3
import tkinter as tk
from clase_calculadora import Calculadora

ventana = tk.Tk()#ventana principal
ventana.title("Calculadora")
cal = Calculadora(ventana)#intanciar la clase Calculadora en la ventana
cal.crear_botones()#llamar al metodo crear_botones de la clase Calculadora
cal.click("")#llamar al metodo click de la clase Calculadora
ventana.geometry("382x425")
ventana.resizable(width=False, height=False)
ventana.configure(background="#393A4B")
ventana.mainloop()