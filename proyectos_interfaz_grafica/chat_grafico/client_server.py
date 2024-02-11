#!/usr/bien/env python3
import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText
  
def send_message(entry_widget, text_widget, client_socket, username):
    mensaje = entry_widget.get()#obtiene el mensaje del cuadro de texto
    client_socket.sendall(mensaje.encode())#envia el mensaje al servidor
    entry_widget.delete(0, END)#borra el mensaje del cuadro de texto
    text_widget.configure(state='normal')#permite escribir en el cuadro de texto
    text_widget.insert(END, f"{username} --> {mensaje}\n")#agrega el mensaje al cuadro de texto
    #print(mensaje)


def receive_message_server(client_socket, text_widget):
    
    while True:
         try:
             mensaje = client_socket.recv(1024).decode()#recibe el mensaje del servidor
             if not mensaje:
                 break
             text_widget.configure(state='normal')#permite escribir en el cuadro de texto
             text_widget.insert(END, f"{mensaje}\n")#agrega el mensaje al cuadro de texto
             text_widget.configure(state='disabled')#no permite escribir en el cuadro de texto
             #     print(mensaje)
         except:
             break
             
def listar_usuarios(client_socket):
    client_socket.sendall("¡usuario".encode())#envia el mensaje al servidor

def salir_usuario(client_socket,username,window):
    client_socket.sendall(f"[+]El usuario ha salido...".encode())#envia el mensaje al servidor
    client_socket.close()
    
    window.destroy()
    window.quit()
   

def client_program():
    host = "localhost"
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = (host, port)
    client_socket.connect(server_adress)

    username = input("Ingrese su nombre de usuario: ")
    client_socket.sendall(username.encode())
    
    #Esto es para la interfaz grafica
    window = Tk()
    window.title("Chat")
    
    #Text widget es para el cuadro de texto
    text_widget = ScrolledText(window, state='disabled')
    text_widget.pack(padx=5, pady=5, fill=BOTH, expand=True)

    #Tengo que usar frame para que el boton este ubicando en la parte inferior
    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=5, fill=BOTH)


    #Entry widget es para el cuadro de texto donde se escribe
    entry_widget = Entry(frame_widget, width=100,font=("Arial", 10))
    entry_widget.bind("<Return>", lambda x: send_message(entry_widget, text_widget, client_socket, username))
    entry_widget.pack(side=LEFT,padx=5, pady=5, fill=BOTH)
     

    #agregar un boton para enviar el mensaje
    send_button = Button(frame_widget, text="Enviar", command=lambda: send_message(entry_widget, text_widget, client_socket, username))
    send_button.pack(side=RIGHT, padx=5, pady=5)
    
    #otro boton para listar usuarios conectados
    listar_boton = Button(window, text="Listar usuarios", command=lambda: listar_usuarios(client_socket))
    listar_boton.pack(padx=5, pady=5)
    
    #boton para salir
    salir_boton = Button(window, text="Salir", command=lambda:  salir_usuario(client_socket,username,window))  
    salir_boton.pack(padx=3, pady=3)

    #thread para recibir mensajes del servidor
    hilo = threading.Thread(target=receive_message_server, args=(client_socket, text_widget))
    hilo.daemon = True
    hilo.start()

    window.mainloop()

if __name__ == "__main__":
    client_program()