'''Representa un artista en el museo'''
class Artista:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
        
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"