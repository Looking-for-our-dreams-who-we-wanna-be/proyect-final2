import json  # 1. Esta es la librería mágica que traduce el archivo

ARCHIVO_JSON = "materias.json"

# --- FUNCIONES DE CARGA Y GUARDADO ---

def cargar_datos():
    """Lee el archivo JSON y lo convierte en lista de Python"""
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("El archivo no existe. Creando lista vacía.")
        return []

def guardar_datos(datos_nuevos):
    """Toma la lista de Python y la escribe en el archivo JSON"""
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        # indent=4 hace que se vea bonito y ordenado en el archivo
        json.dump(datos_nuevos, archivo, indent=4, ensure_ascii=False)
    print(">>> Cambios guardados exitosamente en el archivo.")

# --- LÓGICA DEL COORDINADOR ---

def menu_coordinador():
    materias = cargar_datos() # Cargamos los datos al iniciar
    
    while True:
        print("\n--- SISTEMA COORDINADOR UNEFA ---")
        print("1. Buscar y Modificar Materia")
        print("2. Ver todas las materias")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_y_modificar(materias)
        elif opcion == "2":
            mostrar_todas(materias)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida pajuo.")

def mostrar_todas(lista_materias):
    print("\n--- LISTA DE MATERIAS ---")
    for m in lista_materias:
        estado = "ACTIVA" if m['activa'] else "INACTIVA"
        print(f"[{m['codigo_materia']}] {m['materia']} - Cupo: {m['cupo']} - Estado: {estado}")

def buscar_y_modificar(lista_materias):
    codigo_buscado = input("Ingrese el CÓDIGO de la materia a modificar (ej. MAT0101): ")
    
    materia_encontrada = None
    
    # Buscamos la materia en la lista
    for m in lista_materias:
        if m["codigo_materia"] == codigo_buscado:
            materia_encontrada = m
            break
    
    if not materia_encontrada:
        print("Error: Materia no encontrada.")
        return

    # Si la encontramos, mostramos el menú de edición
    print(f"\nEditando: {materia_encontrada['materia']}")
    print(f"Estado actual: {'Activa' if materia_encontrada['activa'] else 'Inactiva'}")
    print(f"Cupo actual: {materia_encontrada['cupo']}")
    
    print("\n¿Qué desea hacer?")
    print("A. Activar/Desactivar materia")
    print("B. Modificar Cupo")
    print("C. Cancelar")
    
    accion = input("Elija una opción: ").upper()
    
    hay_cambios = False

    if accion == "A":
        # Invertimos el valor: Si es True pasa a False, y viceversa
        estado_nuevo = not materia_encontrada['activa']
        materia_encontrada['activa'] = estado_nuevo
        print(f"Estado cambiado a: {estado_nuevo}")
        hay_cambios = True

    elif accion == "B":
        nuevo_cupo = int(input("Ingrese nuevo cupo: "))
        materia_encontrada['cupo'] = nuevo_cupo
        hay_cambios = True
        
    elif accion == "C":
        print("Operación cancelada.")
        
    # Solo si hubo cambios, llamamos a la función de guardar
    if hay_cambios:
        guardar_datos(lista_materias)

# --- PUNTO DE ARRANQUE ---
# Esto hace que el código arranque solo si ejecutas este archivo
if __name__ == "__main__":
    menu_coordinador()