import json
import os
import time

ARCHIVO_MATERIAS = "materias.json"         
ARCHIVO_INSCRIPCIONES = "horario_estudiante.json" 

HORAS_CLASE = [
    "7:00 - 7:45", "7:45 - 8:30", "8:30 - 9:15", "9:15 - 10:00",
    "10:00 - 10:45", "10:45 - 11:30", "11:30 - 12:15", "12:15 - 1:00"
]

def cargar_json(archivo):
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_json(archivo, datos):
    with open(archivo, "w", encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def ver_oferta_academica():
    materias = cargar_json(ARCHIVO_MATERIAS)
    
    print(f"{'CÓDIGO':<8} | {'MATERIA':<15} | {'CUPO':<5} | {'UC':<3} | {'ESTADO'}")

    
    hay_materias = False
    for m in materias:

        if m.get("activa") == True:
            hay_materias = True

            estado_inscripcion = "Disponible"
            if m["cupo"] <= 0:
                estado_inscripcion = "Agotada"
            uc = m.get("uc", 3)
            
            print(f"{m['codigo_materia']:<10} | {m['materia']:<25} | {m['cupo']:<5} | {uc:<3} | {estado_inscripcion}")
            
    if not hay_materias:
        print(">> No hay materias ofertadas en este momento.")

def inscribir_materia(usuario_cedula):

    ver_oferta_academica()
    
    catalogo = cargar_json(ARCHIVO_MATERIAS)
    inscripciones = cargar_json(ARCHIVO_INSCRIPCIONES)
    
    print(f"\n--- INSCRIPCIÓN DE: {usuario_cedula.upper()} ---")
    codigo = input("Ingrese el CÓDIGO de la materia a inscribir: ").upper()

    materia_encontrada = None
    for m in catalogo:
        if m["codigo_materia"] == codigo:
            materia_encontrada = m
            break

    if not materia_encontrada:
        print("Error: Materia no encontrada.")
        return
    if not materia_encontrada.get("activa"):
        print("Error: La materia no está activa.")
        return
    if materia_encontrada["cupo"] <= 0:
        print("Error: Materia sin cupos.")
        return

    for reg in inscripciones:
        if reg.get("estudiante") == usuario_cedula and reg["codigo_materia"] == codigo:
            print("Ya tienes inscrita esta materia.")
            return

    materia_encontrada["cupo"] -= 1
    guardar_json(ARCHIVO_MATERIAS, catalogo)

    nueva_inscripcion = {
        "estudiante": usuario_cedula,
        "materia": materia_encontrada["materia"],
        "codigo_materia": materia_encontrada["codigo_materia"],
        "dia": materia_encontrada["dia"],
        "bloques": materia_encontrada["bloques"]
    }
    inscripciones.append(nueva_inscripcion)
    guardar_json(ARCHIVO_INSCRIPCIONES, inscripciones)
    
    print(f"¡Inscripción exitosa en {materia_encontrada['materia']}!")
    time.sleep(4.5)

def ver_mi_horario(usuario_cedula):
    todas_inscripciones = cargar_json(ARCHIVO_INSCRIPCIONES)

    mis_materias = []
    for reg in todas_inscripciones:
        if reg.get("estudiante") == usuario_cedula:
            mis_materias.append(reg)
            
    if not mis_materias:
        print(f"\n⚠️ El estudiante {usuario_cedula} no tiene materias inscritas.")
        return

    horario_visual = [["HORA", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]]

    for hora in HORAS_CLASE:

        hora_corta = hora.replace(" ", "") 
        fila = [hora_corta] + ["---"] * 6 
        horario_visual.append(fila)

    mapa_dias = {
        "Lunes": 1, "Martes": 2, "Miércoles": 3, "Miercoles": 3,
        "Jueves": 4, "Viernes": 5, "Sábado": 6, "Sabado": 6
    }
    
    for m in mis_materias:

        nombre_corto = m["materia"][:9] 
        for dia in m["dia"]:
            if dia in mapa_dias:
                columna = mapa_dias[dia]
                for bloque in m["bloques"]:
                    if 0 <= bloque < len(HORAS_CLASE):
                        fila = bloque + 1
                        horario_visual[fila][columna] = nombre_corto
    ancho_total = 78
    print("\n" + "="*ancho_total)
    print(f"HORARIO: {usuario_cedula.upper()}")
    print("="*ancho_total)
    
    for fila in horario_visual:

        print(f"{fila[0]:11} | {fila[1]:9} | {fila[2]:9} | {fila[3]:9} | {fila[4]:9} | {fila[5]:9} | {fila[6]:9}|")
        print("-" * ancho_total)
    
    input("\nPresione Enter...")

def menu_alumno(usuario_cedula):
    while True:
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')

        print(f"PANEL DE ALUMNO: {usuario_cedula.upper()}")
        print("1. Ver Oferta Académica (Materias Activas)")
        print("2. Inscribir Materia")
        print("3. Ver mi Horario")
        print("4. Salir")
        
        opcion = input("\n>> Seleccione una opción: ")
        
        if opcion == "1":
            ver_oferta_academica()
            input("\nPresione Enter para volver...")
        elif opcion == "2":
            inscribir_materia(usuario_cedula)
        elif opcion == "3":
            ver_mi_horario(usuario_cedula)
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":

    usuario = "V-12345678" 
    
    print(f"--- MODO PRUEBA AUTOMÁTICO CON: {usuario} ---")
    menu_alumno(usuario)
    