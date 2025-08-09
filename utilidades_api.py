from PIL import Image
import requests
from io import BytesIO

def mostrar_imagen(url): 
    '''
    Muestra una imagen desde una URL si está disponible
'''    
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
    except:
        print("No se pudo cargar la imagen")

def obtener_nacionalidades(obras): 
    '''
    Obtiene una lista de nacionalidades únicas de los artistas de las obras
    '''
    nacionalidades = set()
    for obra in obras:
        if obra.artista.nacionalidad:
            nacionalidades.add(obra.artista.nacionalidad)
    return sorted(nacionalidades)

def obtener_autores(obras): 
    '''
    Obtiene una lista de autores de las obras del departamento seleccionado
    '''
    autores = set()
    for obra in obras:
        if obra.artista.nombre:
            autores.add(obra.artista.nombre.strip()) 
    return sorted(autores)