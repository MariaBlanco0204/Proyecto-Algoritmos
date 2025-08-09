import requests
from departamento import Departamento
from artista import Artista
from obra import Obra

def obtener_departamentos(): 
    '''
    Obtiene la lista de departamentos desde la API del Museo Metropolitano
    '''
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    data = response.json()
    
    departamentos = []
    for dept in data['departments']:
        departamentos.append(Departamento(dept['departmentId'], dept['displayName']))
    
    return departamentos

def obtener_obras_por_departamento(departamento_id): 
    '''
      Obtiene las obras de un departamento específico
    '''
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={departamento_id}"
    response = requests.get(url)
    data = response.json()
    
    print(f'Se encontraron: {data['total']} obras en el departamento {departamento_id}')
    print("Filtrando obras...")
    obras = [] 
    '''
    Lista para almacenar las obras obtenidas
    '''
    for obra_id in data['objectIDs'][:10]: 
        '''
        Limita las obras para evitar sobrecarga de la API
        '''
        obra_data = obtener_detalle_obra(obra_id)
        if obra_data:
            obras.append(obra_data)
    
    return obras

def obtener_detalle_obra(obra_id): 
    '''
     Obtiene los detalles de una obra específica
     '''
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
    response = requests.get(url)
    data = response.json()
    
    if not data.get('artistDisplayName'): 
        '''
          Verifica si la obra tiene un artista asociado
        '''
        return None
    
    artista = Artista( 
        nombre=data['artistDisplayName'],
        nacionalidad=data.get('artistNationality', 'Desconocida'),
        fecha_nacimiento=data.get('artistBeginDate', 'Desconocida'),
        fecha_muerte=data.get('artistEndDate', 'Desconocida')
    )
    '''
         Crea un objeto de tipo Artista
         '''
    
    departamento = Departamento(  
        data.get('departmentId', 0),
        data.get('department', 'Desconocido')  
    )
    '''
        Crea un objeto de tipo Departamento
        '''
    
    obra = Obra ( 
        id=data['objectID'],
        titulo=data['title'],
        artista=artista,
        departamento=departamento,
        tipo=data['classification'],
        fecha_creacion=data['objectDate'],
        imagen_url=data.get('primaryImageSmall', '')
    )
    '''
        Crea un objeto de tipo Obra
    '''
    
    return obra

def obtener_obras_por_nacionalidad(obras, nacionalidad): 
    '''
    Filtra obras por nacionalidad del artista
    '''
    obras_filtradas = []
    for obra in obras:
        if obra.artista.nacionalidad.lower() == nacionalidad.lower():
            obras_filtradas.append(obra)
    return obras_filtradas

def obtener_obras_por_autor(obras, nombre_autor): 
    '''
     Filtra obras por nombre del autor
     '''
    obras_filtradas = []
    for obra in obras:
        if nombre_autor.lower() in obra.artista.nombre.lower():
            obras_filtradas.append(obra)
    return obras_filtradas
