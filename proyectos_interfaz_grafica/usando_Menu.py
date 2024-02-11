import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


ventana = tk.Tk()
ventana.title("Usando Menu")

def nuevo_archivo():
    print("Creando un nuevo archivo")

def abrir_archivo():
    ruta_archivo = tk.filedialog.askopenfilename()
    messagebox.showinfo("Abrir archivo", ruta_archivo)


# Crear un menu
barra_menu = tk.Menu(ventana)

# Crear elementos de menu archivo_menu
archivo_menu = tk.Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo", command=nuevo_archivo)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar")
archivo_menu.add_separator()   
archivo_menu.add_command(label="Salir", command=ventana.quit)

# Crear elementos de menu edicion_menu
edicion_menu = tk.Menu(barra_menu, tearoff=0)
edicion_menu.add_command(label="Copiar")
edicion_menu.add_command(label="Cortar")
edicion_menu.add_command(label="Pegar")


# Agregar elementos de menu a la barra de menu
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edicion", menu=edicion_menu)


#configurar ventana para usar la barra de menu
ventana.config(menu=barra_menu)




ventana.geometry("400x200")
ventana.mainloop()
