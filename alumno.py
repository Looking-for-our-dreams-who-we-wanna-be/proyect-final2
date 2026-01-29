import json
import os

from app import guardar_datos
ARCHIVO_DB = "materias.json"
Archivo_DB = "registroalumnos.json"


def cargar_datos():
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, "r") as archivo:
                return json.load(archivo)
        except:
            return print("No se encontró el archivo materias.json.")
def guardar_datos(lista_materias):
    with open(ARCHIVO_DB, "w") as archivo:
        json.dump(lista_materias, archivo, indent=4)

oferta_materias = cargar_datos()
cargar_datos()

def inscribir_materia():
    
    oferta_materias = cargar_datos()
    
    if not oferta_materias:
        return
    disponibilidad = False
    for materia in oferta_materias:
        if materia["activa"] == True and materia["cupo"] > 0:
            disponibilidad = True
            break
    codigo = input("Ingrese el código de la materia: ").upper()
    materia_encontrada = None

    for materia in oferta_materias:
        if materia["codigo_materia"] == codigo or materia["materia"].upper() == codigo:
            materia_encontrada = materia
            break 
    if not materia_encontrada:
        print("Materia no encontrada")
        return
    if materia_encontrada["activa"] == False:
        print(f"La materia '{materia_encontrada['materia']}' no está activa.")
        return

    if materia_encontrada["cupo"] > 0:
        materia_encontrada["cupo"] -= 1      
        print("Inscripción lista en: " + materia_encontrada["materia"])
        guardar_datos(oferta_materias)
        return
    else:
        print("No quedan cupos.")
        return
inscribir_materia()