import json
import os
import time

ARCHIVO_DB_COORDINADOR = "materias.json"       
ARCHIVO_DB_PROFESOR = "oferta_academica.json"  

def cargar_datos(archivo):
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_datos(archivo, lista_datos):
    try:
        with open(archivo, "w", encoding='utf-8') as f:
            json.dump(lista_datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error guardando: {e}")

def limpiar_pantalla():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def ver_materias_disponibles():
    catalogo = cargar_datos(ARCHIVO_DB_COORDINADOR)
    print("\n" + "="*60)
    print(f"{'CÓDIGO':<10} | {'MATERIA':<25} | {'ESTADO'}")
    print("="*60)
    
    hay = False
    for m in catalogo:
        if m.get("activa"):
            hay = True
            print(f"{m['codigo_materia']:<10} | {m['materia']:<25} | DISPONIBLE")
            
    if not hay: print(">> No hay materias activas disponibles.")
    print("="*60)
    return catalogo

def ofertar_materia(nombre_profesor):
    print(f"\n--- OFERTAR MATERIA ({nombre_profesor}) ---")
    ver_materias_disponibles()
    catalogo = cargar_datos(ARCHIVO_DB_COORDINADOR)
    ofertas = cargar_datos(ARCHIVO_DB_PROFESOR)

    codigo = input("\nIngrese CÓDIGO de la materia a dictar: ").strip().upper()
    
    materia_base = None
    for m in catalogo:
        if m["codigo_materia"] == codigo:
            materia_base = m
            break
    
    if not materia_base:
        print("Materia no encontrada en el catálogo.")
        input("Enter para continuar...")
        return
        
    if not materia_base.get("activa"):
        print("Materia inactiva.")
        input("Enter para continuar...")
        return

    seccion = input("Sección (Ej: A, B, U1): ").strip().upper()
    try:
        cupo = int(input("Cupo máximo: "))
    except:
        print("El cupo debe ser un número.")
        return

    nueva_oferta = {
        "profesor": nombre_profesor,
        "codigo_materia": materia_base["codigo_materia"],
        "materia": materia_base["materia"],
        "seccion": seccion,
        "cupo_total": cupo,
        "cupo_disponible": cupo,
        "dia": materia_base.get("dia", []),
        "bloques": materia_base.get("bloques", [])
    }
    
    ofertas.append(nueva_oferta)
    guardar_datos(ARCHIVO_DB_PROFESOR, ofertas)
    print(f"Sección {seccion} de {materia_base['materia']} creada exitosamente.")
    time.sleep(1.5)

def ver_mis_ofertas(nombre_profesor):
    ofertas = cargar_datos(ARCHIVO_DB_PROFESOR)
    print(f"\n=== MATERIAS DE: {nombre_profesor.upper()} ===")
    
    encontrado = False
    for o in ofertas:

        if o.get("profesor", "").upper() == nombre_profesor.upper():

            materia = o.get("materia", "Sin nombre")
            seccion = o.get("seccion", "?")
            c_disp = o.get("cupo_disponible", 0) 
            c_total = o.get("cupo_total", 0)
            
            print(f"• {materia} (Sec. {seccion})")
            print(f"  Cupos Disponibles: {c_disp} / {c_total}")
            print("-" * 40)
            encontrado = True
            
    if not encontrado:
        print(">> No tiene materias ofertadas.")
    
    input("\nPresione Enter para volver...")

def menu_profesor(usuario_nombre):
    while True:
        limpiar_pantalla()
        print(f"\nPANEL DOCENTE: {usuario_nombre}")
        print("1. Ver Catálogo General")
        print("2. Ofertar Materia")
        print("3. Ver mis materias")
        print("4. Salir")
        
        op = input("\n>> Opción: ")
        
        if op == "1":
            ver_materias_disponibles()
            input("Enter para volver...")
        elif op == "2":
            ofertar_materia(usuario_nombre)
        elif op == "3":
            ver_mis_ofertas(usuario_nombre)
        elif op == "4":
            break
