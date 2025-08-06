from artista import artista
from departamento import departamento 

"""representa una obra de arte en el museo"""
class obra:
    def __init__(self, id, titulo, artista, departamento, tipo, fecha_creacion, imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento 
        self.tipo = tipo
        self.fceha_creacion = fecha_creacion
        self.imagen_url = imagen_url
        
    def __str__(self):
        return f"{self.id}:{self.titulo} - {self.artista}"