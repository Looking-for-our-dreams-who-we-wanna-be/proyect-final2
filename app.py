import json
import os

ARCHIVO_DB = "materias.json"

bhoras = {
    0: "7:00 - 7:45", 1: "7:45 - 8:30", 2: "8:30 - 9:15", 3: "9:15 - 10:00",
    4: "10:00 - 10:45", 5: "10:45 - 11:30", 6: "11:30 - 12:15", 7: "12:15 - 13:00"
}

datos_iniciales = [
    {
        "codigo_materia": "MAT0101", "materia": "Matematicas I", 
        "dia": [], "cupo": 0, "bloques": [], "seccion": "", "activa": False
    },
    {
        "codigo_materia": "FIS0101", "materia": "Fisica I", 
        "dia": [], "cupo": 0, "bloques": [], "seccion": "D1", "activa": False
    },
    {
        "codigo_materia": "QUI0101", "materia": "Quimica I", 
        "dia": [], "cupo": 0, "bloques": [], "seccion": "D1", "activa": False
    },
    {
        "codigo_materia": "LOG0101", "materia": "Geometría analítica",
        "dia": [], "cupo": 0, "bloques": [], "seccion": "D1", "activa": False
    }
]

def cargar_datos():
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, "r") as archivo:
                return json.load(archivo)
        except:
            return datos_iniciales
    else:
        return print("No se encontró el archivo materias.json.")

def guardar_datos(lista_materias):
    with open(ARCHIVO_DB, "w") as archivo:
        json.dump(lista_materias, archivo, indent=4)

oferta_materias = cargar_datos()


def crearoferta_materias():
    print ("\n--- CREAR OFERTA DE MATERIAS ---")

    codigo = input("Ingrese el código de la materia: ")
    materia_encontrada = None
    
    for materia in oferta_materias:
        if materia["codigo_materia"] == codigo:
            materia_encontrada = materia
            break
        elif materia["materia"] == codigo:
            materia_encontrada = materia
            break 
            
    if not materia_encontrada:
        print(" Código no encontrado en el catálogo.")
        return 

    print(f" Editando: {materia_encontrada['materia']}")

    dia_input = input("Ingrese el día (ej, Lunes): ").capitalize()
    if dia_input in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]:
        materia_encontrada["dia"] = [dia_input]
        print(f"   -> Día {dia_input} guardado.")
    else:
        print(" Día inválido.")
        return

    try:
        cupo = int(input("Ingrese el cupo (Máx 50): "))
        if cupo <= 0: 
            print(" El cupo debe ser positivo.")
            return
        elif cupo > 50: 
            print(" El cupo máximo es 50.")
            return
        else: 
            materia_encontrada["cupo"] = cupo
            print(f"   -> Cupo {cupo} guardado.")
    except ValueError:
        print(" Error: Ingrese solo números.")
        return

    entrada_bloques = input("Ingrese los bloques horarios (ej. 0,1): ")
    try:
        lista_bloques = [int(x) for x in entrada_bloques.split(",")]
        bloques_validos = []
        for num in lista_bloques:
            if num in bhoras:
                bloques_validos.append(num)
            else:
                print(f" Bloque {num} no existe.")
        
        if bloques_validos:
            materia_encontrada["bloques"] = bloques_validos 
            print("Bloques guardados.")
        else:
            print(" No se guardaron bloques válidos.")
            return
    except ValueError:
        print(" Error en formato de horas.")
        return

    seccion = input("Ingrese la sección (Enter para default): ")
    if seccion != "":
        materia_encontrada["seccion"] = seccion 

    materia_encontrada["activa"] = True 

    print("\n--- ASÍ QUEDÓ TU MATERIA ---")
    print(f"Materia: {materia_encontrada['materia']}")
    print(f"Código:  {materia_encontrada['codigo_materia']}")
    print(f"Cupo:    {materia_encontrada['cupo']}")
    print(f"Día:     {materia_encontrada['dia']}")
    print(f"Bloques: {materia_encontrada['bloques']}")
    print(f"Activa:  {materia_encontrada['activa']}")
    
    guardar_datos(oferta_materias)
    print(" ¡Cambios guardados en materias.json!")


crearoferta_materias()

#rehice todo el codigo porque estaba mal estructurado y con errores aparte se me olvido que queria hacer.
#teoricamente ya funciona, lee perono guarda nada aun.

import json

ARCHIVO_JSON = "materias.json"



def cargar_datos():

    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("El archivo no existe. Creando lista vacía.")
        return []

def guardar_datos(datos_nuevos):

    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:

        json.dump(datos_nuevos, archivo, indent=4, ensure_ascii=False)
    print(">>> Cambios guardados exitosamente en el archivo.")


def menu_coordinador():
    materias = cargar_datos()
    
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

    for m in lista_materias:
        if m["codigo_materia"] == codigo_buscado:
            materia_encontrada = m
            break
    
    if not materia_encontrada:
        print("Error: Materia no encontrada.")
        return

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
        
    if hay_cambios:
        guardar_datos(lista_materias)

if __name__ == "__main__":
    menu_coordinador()
