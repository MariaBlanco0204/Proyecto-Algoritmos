from artista import Artista
from departamento import Departamento

class Obra: 
    '''
    Representa una obra de arte en el museo
    '''
    def __init__(self, id, titulo, artista, departamento, tipo, fecha_creacion, imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.imagen_url = imagen_url
        
    def __str__(self):
        return f"{self.id}: {self.titulo} - {self.artista.nombre}"