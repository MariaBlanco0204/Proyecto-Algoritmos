from PIL import Image
import requests
from io import BytesIO

"""muestra una imagen desde un URL si esta disponible"""
def mostrar_imagen(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
    except:
        print("No se pudo cargar la imagen")

"""obtiene una lista de nacionalidades unicas de los artistas de las obras"""
def obtener_nacionalidades(obras):
    nacionalidades = set()
    for obra in obras:
        if obra.artista.nacionalidad:
            nacionalidades.add(obra.artista.nacionalidad)
    return sorted(nacionalidades)

"""obtiene una lista de autores de las obras del departamento seleccionado"""
def obtener_autores(obras):
    autores = set()
    for obra in obras:
        if obra.artista.nombre:
            autores.add(obra.artista.nombre.strip())
    return sorted(autores)