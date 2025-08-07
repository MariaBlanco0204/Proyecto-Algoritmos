import requests
from departamento import Departamento
from artista import Artista
from obra import Obra

"""Obtiene la lista de departamentos desde la API del Museo Metropolitano"""

def obtener_departamentos(): 
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    data = response.json()
    
    departamentos = []
    for dept in data['departments']:
        departamentos.append(Departamento(dept['departmentId'], dept['displayName']))
    
    return departamentos

"""Obtiene las obras de un departamento específico"""

def obtener_obras_por_departamento(departamento_id): 
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={departamento_id}"
    response = requests.get(url)
    data = response.json()
    
    print(f'Se encontraron: {data['total']} obras en el departamento {departamento_id}')
    print("Filtrando obras...")
    obras = []  
    
    """Lista para almacenar las obras obtenidas"""

    """Limita las obras para evitar sobrecarga de la API"""

    for obra_id in data['objectIDs'][:10]: 
        obra_data = obtener_detalle_obra(obra_id)
        if obra_data:
            obras.append(obra_data)
    
    return obras

"""Obtiene los detalles de una obra específica"""

def obtener_detalle_obra(obra_id): 
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
    response = requests.get(url)
    data = response.json()

    """Verifica si la obra tiene un artista asociado"""

    if not data.get('artistDisplayName'): 
        return None
    
    """Crea un objeto de tipo Artista"""
    
    artista = Artista(
        nombre=data['artistDisplayName'],
        nacionalidad=data.get('artistNationality', 'Desconocida'),
        fecha_nacimiento=data.get('artistBeginDate', 'Desconocida'),
        fecha_muerte=data.get('artistEndDate', 'Desconocida')
    )

    """Crea un objeto de tipo Departamento"""

    departamento = Departamento(  
        data.get('departmentId', 0),
        data.get('department', 'Desconocido')  
    )

    """Crea un objeto de tipo Obra"""

    obra = Obra( 
        id=data['objectID'],
        titulo=data['title'],
        artista=artista,
        departamento=departamento,
        tipo=data['classification'],
        fecha_creacion=data['objectDate'],
        imagen_url=data.get('primaryImageSmall', '')
    )
    
    return obra

"""Filtra obras por nacionalidad del artista"""

def obtener_obras_por_nacionalidad(obras, nacionalidad):
    obras_filtradas = []
    for obra in obras:
        if obra.artista.nacionalidad.lower() == nacionalidad.lower():
            obras_filtradas.append(obra)
    return obras_filtradas

"""Filtra obras por nombre del autor""" 

def obtener_obras_por_autor(obras, nombre_autor): 
    obras_filtradas = []
    for obra in obras:
        if nombre_autor.lower() in obra.artista.nombre.lower():
            obras_filtradas.append(obra)
    return obras_filtradas