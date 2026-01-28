import json
import os

from app import guardar_datos
ARCHIVO_DB = "materias.json"
Archivo_DB = "inscripciones.json"


def cargar_datos():
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, "r") as archivo:
                return json.load(archivo)
        except:
            return []

oferta_materias = cargar_datos()
cargar_datos()

def inscribir_materia():
    codigo = input("Ingrese el código de la materia a inscribir: ").upper()
    materia_encontrada = None
    for materia in oferta_materias:
        if materia["codigo_materia"] == codigo:
            materia_encontrada = materia
            print(" Materia encontrada " + materia_encontrada["materia"])
            break
        elif materia["materia"].upper() == codigo:
            materia_encontrada = materia
            break
    if not materia_encontrada:
        print(" Materia no encontrada.")
        return
    cupos_disponibles = materia_encontrada["cupo"]
    if cupos_disponibles >= 0:
        materia_encontrada["cupo"] -= 1
        print(" Inscripción exitosa en la materia: " + materia_encontrada["materia"])
        guardar_datos(oferta_materias)
        return
    elif cupos_disponibles <= 0:
        print(" No hay cupos disponibles para esta materia.")
        return
inscribir_materia()