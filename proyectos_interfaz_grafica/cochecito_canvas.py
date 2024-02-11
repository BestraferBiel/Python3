import tkinter as tk

def dibujar_cochecito(canvas):
    # Cuerpo del coche
    canvas.create_rectangle(50, 100, 250, 180, fill="blue")

    # Techo
    canvas.create_polygon(50, 100, 150, 50, 250, 100, fill="blue")

    # Ruedas
    canvas.create_oval(80, 180, 120, 220, fill="black")
    canvas.create_oval(180, 180, 220, 220, fill="black")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Dibujar Cochecito")

# Crear el lienzo (Canvas)
canvas = tk.Canvas(ventana, width=300, height=250, bg="white")
canvas.pack()

# Dibujar el cochecito en el lienzo
dibujar_cochecito(canvas)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
