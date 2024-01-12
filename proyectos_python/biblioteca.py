#!/usr/bin/env python3


class Libro: 
    def __init__(self, titulo, autor, genero, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.id_libro = id_libro
        self.esta_prestado = False
    def __str__(self):
        return f"{self.id_libro}:Libro {self.titulo} de {self.autor}"
    def __repr__(self):
       return self.__str__()

 
class Biblioteca:
    def __init__(self):
        self.libros = {}
    
    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros.keys():
            self.libros.update({libro.id_libro: libro})
        else:    
            print("[+]El libro ya se encuentra en la biblioteca")
    
    @property
    def mostrar_libros(self):
       return [libro for libro in self.libros.values() if not libro.esta_prestado]#me devuelve el libro que no esta prestado esta representacion es una lista 
     
    @property
    def mostrar_libros_prestados(self):
       return [libro for libro in self.libros.values() if libro.esta_prestado]
#Este codigo es lo mismo que el de arriba pero con un for
     #def mostrar_libros(self):
      #  libros_disponibles = []
       # for libro in self.libros.values():
        #    if not libro.esta_prestado:
         #       libros_disponibles.append(libro)
        #return libros_disponibles
    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
            print(f"[+]Se presto el libro:{self.libros[id_libro].titulo}")
        else:
           print("[+]El libro no se encuentra en la biblioteca esta prestado o el id es incorrecto")


class Biblioteca_Infantil(Biblioteca):
    def __init__(self): 
        super().__init__()
        self.libros_para_ninos = {}
        
    def agregar_libro(self, libro,es_para_ninos):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id_libro] = es_para_ninos
   
    def prestar_libro_ninos(self, id_libro,es_para_ninos):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado and self.libros_para_ninos[id_libro] == es_para_ninos:
            self.libros[id_libro].esta_prestado = True
            print(f"[+]Se presto el libro:{self.libros[id_libro].titulo}")
        else:
           print("[+]El libro no se encuentra en la biblioteca esta prestado o el id es incorrecto")
    @property
    def mostrar_libros_para_ninos(self):       
      return self.libros_para_ninos
if __name__ == "__main__":


 biblioteca = Biblioteca()
 biblioteca_infantil = Biblioteca_Infantil()

 libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasia",1001)
 libro2 = Libro("El hobbit", "J.R.R. Tolkien", "Fantasia", 1002)   
 libro3 = Libro("Harry Potter", "J.K. Rowling", "Fantasia", 1003)
 libro4 = Libro("El nombre del viento", "Patrick Rothfuss", "Fantasia", 1004)
 libro5 = Libro("El temor de un hombre sabio", "Patrick Rothfuss", "Fantasia", 1005)
 libro6 = Libro("El imperio final", "Brandon Sanderson", "Fantasia", 1006)

 biblioteca.agregar_libro(libro1)
 biblioteca.agregar_libro(libro2)
 biblioteca.agregar_libro(libro4)
 biblioteca.agregar_libro(libro3)
 biblioteca_infantil.agregar_libro(libro5,es_para_ninos=True)
 biblioteca_infantil.agregar_libro(libro6,es_para_ninos=False)


 #print(biblioteca.libros)
 #print(biblioteca.libros)
 #print(biblioteca.mostrar_libros)#me devuelve el libro que no esta prestado y lo comverti en @ property para no usar parentesis
 #print(libro2)

biblioteca.prestar_libro(1004)
biblioteca.prestar_libro(1001)
biblioteca_infantil.prestar_libro_ninos(1005,es_para_ninos=True)
biblioteca_infantil.prestar_libro_ninos(1006,es_para_ninos=False)
print(f"\n[+]Los libros en la biblioteca:{biblioteca.mostrar_libros}")
print(f"\n[+]Los libros prestados:{biblioteca.mostrar_libros_prestados}")


print(f"\n[+]Los libros prestados:{biblioteca_infantil.mostrar_libros_para_ninos}")

