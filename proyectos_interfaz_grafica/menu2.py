import tkinter as tk

def mostrar_mensaje():
    etiqueta_resultado.config(text="Menú seleccionado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Menú")

# Función que se ejecutará al hacer clic en una opción del menú
def accion_menu(opcion):
    etiqueta_resultado.config(text=f"Menú seleccionado: {opcion}")

# Crear un menú
barra_menu = tk.Menu(ventana)

# Crear un menú desplegable llamado "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=lambda: accion_menu("Abrir"))
menu_archivo.add_command(label="Guardar", command=lambda: accion_menu("Guardar"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

# Agregar el menú "Archivo" a la barra de menú
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Configurar la ventana para usar la barra de menú
ventana.config(menu=barra_menu)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.geometry("300x200")
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
