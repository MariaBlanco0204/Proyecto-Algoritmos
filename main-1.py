from datos_api import obtener_departamentos, obtener_obras_por_departamento, obtener_obras_por_nacionalidad, obtener_obras_por_autor
from menu import menu_principal, mostrar_obras, mostrar_detalles
from utilidades_api import obtener_nacionalidades, obtener_autores

def main(): 
    '''
    Funcion principal del sistema
    '''
    departamentos = obtener_departamentos() 
    '''Se obtienen los departamentos de la API'''
    obras = []
    
    '''Ciclo infinito del flujo principal del programa hasta que se seleccione salir'''
    while True:
        opcion = menu_principal()
        
        if opcion == 1:
            print("\nDepartamentos disponibles:")
            for dept in departamentos:
                print(f"{dept.id}: {dept.nombre}")
            
            try:
                dept_id = int(input("\nIngrese el ID del departamento: "))
                obras = obtener_obras_por_departamento(dept_id)
                mostrar_obras(obras)
            except ValueError:
                print("ID inválido.")
        
        elif opcion == 2:
            if not obras:
                print("Primero cargue obras desde un departamento.")
                continue
                
            nacionalidades = obtener_nacionalidades(obras)
            print("\nNacionalidades disponibles:")
            for i, nac in enumerate(nacionalidades, 1):
                print(f"{i}. {nac}")
            
            try:
                seleccion = int(input("\nSeleccione una nacionalidad: ")) - 1
                if 0 <= seleccion < len(nacionalidades):
                    obras_filtradas = obtener_obras_por_nacionalidad(obras, nacionalidades[seleccion])
                    mostrar_obras(obras_filtradas)
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Por favor ingrese un número válido.")
        
        elif opcion == 3:
            if not obras:
                print("Primero cargue obras desde un departamento.")
                continue
                
            autores = obtener_autores(obras)
            print("\nAutores disponibles:")
            for i, autor in enumerate(autores, 1):
                print(f"{i}. {autor}")

            try:
                seleccion = int(input("\nSeleccione un autor: "))
                if 1 <= seleccion <= len(autores):
                    nombre = autores[seleccion - 1]
                else:
                    print("Número inválido.")
                    continue
                
                obras_filtradas = obtener_obras_por_autor(obras, nombre)
                mostrar_obras(obras_filtradas)
            
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == 4:
            print("Saliendo de la Colección de Arte -MetroArt-")
            break
        
        else:
            print("Opción no válida. Por favor intente nuevamente.")
        
        if obras:
            print("\nDetalles de la obra")
            print("Ingrese ID: ")
            try:
                obra_id = int(input("ID: "))
                if obra_id != 0:
                    obra_seleccionada = None
                    for obra in obras:
                        if obra.id == obra_id:
                            obra_seleccionada = obra
                            break
                    mostrar_detalles(obra_seleccionada)
            except ValueError:
                print("Entrada inválida.")

if __name__ == "__main__":
    main() 
    '''Llamado a la función principal'''