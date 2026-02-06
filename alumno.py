import json
import os
import time

ARCHIVO_MATERIAS = "materias.json"
ARCHIVO_INSCRIPCIONES = "horario_estudiante.json"

HORAS_CLASE = [
    "7:00-7:45", "7:45-8:30", "8:30-9:15", "9:15-10:00",
    "10:00-10:45", "10:45-11:30", "11:30-12:15"
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
    try:
        with open(archivo, "w", encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error guardando archivo: {e}")

def limpiar_pantalla():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def ver_oferta_academica():
    materias = cargar_json(ARCHIVO_MATERIAS)
    print("\n" + "="*80)
    print(f"{'CÓDIGO':<10} | {'MATERIA':<25} | {'CUPO':<5} | {'UC':<3} | {'ESTADO'}")
    print("="*80)
    
    hay_datos = False
    for m in materias:
        if m.get("activa"):
            hay_datos = True
            estado = "Disponible" if m["cupo"] > 0 else "Agotada"

            uc_valor = m.get('uc', 3) 
            print(f"{m['codigo_materia']:<10} | {m['materia']:<25} | {m['cupo']:<5} | {uc_valor:<3} | {estado}")
            
    if not hay_datos:
        print(">> No hay materias activas ofertadas por la coordinación.")
    print("="*80)

def inscribir_materia(usuario_cedula):
    ver_oferta_academica()
    catalogo = cargar_json(ARCHIVO_MATERIAS)
    inscripciones = cargar_json(ARCHIVO_INSCRIPCIONES)
    
    print(f"\n--- INSCRIPCIÓN: {usuario_cedula.upper()} ---")
    codigo = input("Ingrese el CÓDIGO de la materia: ").strip().upper()

    materia_encontrada = None
    indice_materia = -1
    
    for i, m in enumerate(catalogo):
        if m["codigo_materia"] == codigo:
            materia_encontrada = m
            indice_materia = i
            break

    if not materia_encontrada:
        print("Materia no encontrada.")
        input("Presione Enter para continuar...")
        return
    
    if not materia_encontrada.get("activa"):
        print("La materia no está activa.")
        input("Presione Enter para continuar...")
        return
        
    if materia_encontrada["cupo"] <= 0:
        print("No hay cupos disponibles.")
        input("Presione Enter para continuar...")
        return

    for reg in inscripciones:
        if reg.get("estudiante") == usuario_cedula and reg["codigo_materia"] == codigo:
            print("⚠️ Ya tienes inscrita esta materia.")
            input("Presione Enter para continuar...")
            return

    catalogo[indice_materia]["cupo"] -= 1

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
    time.sleep(1.5)

def ver_mi_horario(usuario_cedula):
    todas = cargar_json(ARCHIVO_INSCRIPCIONES)

    mis_materias = []
    for r in todas:
        if r.get("estudiante") == usuario_cedula:
            mis_materias.append(r)
    
    if not mis_materias:
        print(f"\n{usuario_cedula} no tiene materias inscritas.")
        input("Presione Enter para volver...")
        return

    horario_visual = [["HORA", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]]

    for hora in HORAS_CLASE:

        horario_visual.append([hora, "---", "---", "---", "---", "---", "---"])

    mapa_dias = {
        "Lunes": 1, "Martes": 2, "Miércoles": 3, "Miercoles": 3, 
        "Jueves": 4, "Viernes": 5, "Sábado": 6, "Sabado": 6
    }

    for m in mis_materias:
        nombre = m["materia"][:12] 
        
        for dia in m["dia"]:
            if dia in mapa_dias:
                col = mapa_dias[dia]
                for b in m["bloques"]:

                    if isinstance(b, int) and 0 <= b < len(HORAS_CLASE):
                        horario_visual[b + 1][col] = nombre

    print("\n" + "="*95)
    print(f"HORARIO DE CLASES: {usuario_cedula.upper()}")
    print("="*95)
    
    for fila in horario_visual:

        print(f"{fila[0]:12} | {fila[1]:12} | {fila[2]:12} | {fila[3]:12} | {fila[4]:12} | {fila[5]:12} | {fila[6]:12}|")
        print("-" * 110)
    
    input("\nPresione Enter para volver...")

def menu_alumno(usuario_cedula):
    while True:
        limpiar_pantalla()
        print(f"   PANEL DE ALUMNO: {usuario_cedula}")
        print("1. Ver Oferta Académica")
        print("2. Inscribir Materia")
        print("3. Ver mi Horario")
        print("4. Salir")
        
        op = input("\n>> Opción: ")
        
        if op == "1":
            ver_oferta_academica()
            input("\nPresione Enter para continuar...")
        elif op == "2":
            inscribir_materia(usuario_cedula)
        elif op == "3":
            ver_mi_horario(usuario_cedula)
        elif op == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    menu_alumno("ALUMNO_PRUEBA")