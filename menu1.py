from utilidades_api import mostrar_imagen

"""Muestra el menú principal y devuelve la opción seleccionada"""

def menu_principal(): 
    print("\nColección de Arte -MetroArt- ")
    print("-> 1. Buscar por departamento")
    print("-> 2. Buscar por nacionalidad")
    print("-> 3. Buscar por autor")
    print("-> 4. Salir")
    
    try:
        opcion = int(input("\nSeleccione una opción: ")) 
        return opcion
    except ValueError:
        print("Por favor ingrese un número válido.")
        return menu_principal()
    
"""Muestra las obras relacionadas con el departamento seleccionado"""

def mostrar_obras(obras): 
    if not obras:
        print("No se encontraron obras")
        return
    
    print("\nObras encontradas:")
    for obra in obras:
        print(obra)

"""Muestra los detalles de la obra seleccionada"""

def mostrar_detalles(obra):
    if not obra:
        print("No se encontró la obra solicitada.")
        return
    
    print("\nDetalles de la obra: ")
    print(f"Título: {obra.titulo}")
    print(f"Artista: {obra.artista.nombre}")
    print(f"Nacionalidad: {obra.artista.nacionalidad}")
    print(f"Fecha nacimiento: {obra.artista.fecha_nacimiento}")
    print(f"Fecha muerte: {obra.artista.fecha_muerte}")
    print(f"Tipo: {obra.tipo}")
    print(f"Año de creación: {obra.fecha_creacion}")

    """Si la obra tiene una imagen asociada, permite elegir si verla o no"""

    if obra.imagen_url: 
        while True:
            print("Esta obra tiene una imagen asociada. ¿Desea ver la imagen de la obra?")
            print("Ingrese 's' para sí o 'n' para no")
            respuesta = input().lower()
            
            if respuesta == 's':
                mostrar_imagen(obra.imagen_url)
                break
            elif respuesta == 'n':
                break 
            else:
                print("Por favor ingrese 's' para sí o 'n' para no.")