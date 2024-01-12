#!/usr/bin/env python3
import pickle
from notas import Nota



class GestorNotas:
    def __init__(self,archivos_notas="Gestion_notas/nota.pkl"):
        self.archivos_notas = archivos_notas
        
        try:
            with open(self.archivos_notas,"rb") as archivo:
                self.notas = pickle.load(archivo)
        except FileNotFoundError:
            self.notas = []
    
    def guardar_notas(self):
        with open(self.archivos_notas,"wb") as archivo:
            pickle.dump(self.notas,archivo)

    def agregar_nota(self,contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()       
    
    def leer_notas(self):
        for i ,nota in enumerate(self.notas):
            if nota.estado:
             print(f" {i} : {nota}")
    
    def buscar_nota(self,texto_buscar):
        for nota in self.notas:
            if nota.contenido.find(texto_buscar) != -1:
                return(nota)        
    def eliminar_nota(self,texto_a_eliminar):
        for nota in self.notas:
            if nota.contenido.find(texto_a_eliminar) != -1:
               nota.estado = False
               return(nota)
        else: 
            print("\n[!]No se encontro la nota")        
