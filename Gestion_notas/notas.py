#1/usr/bin/env python3

class Nota:
    def __init__(self,contenido):
        self.contenido = contenido
        self.estado = True

    def __str__(self):
        return f"{self.contenido} - {self.estado}"