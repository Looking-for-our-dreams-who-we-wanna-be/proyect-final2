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
    with open(archivo, "w", encoding='utf-8') as f:
        json.dump(lista_datos, f, indent=4, ensure_ascii=False)


def ver_materias_disponibles():

    catalogo = cargar_datos(ARCHIVO_DB_COORDINADOR)
    
    print("\n" + "="*50)
    print(f"{'CÓDIGO':<10} | {'MATERIA':<25} | {'ESTADO'}")
    print("="*50)
    
    materias_activas = []
    
    for m in catalogo:
        if m.get("activa") == True:
            print(f"{m['codigo_materia']:<10} | {m['materia']:<25} | 🟢 DISPONIBLE")
            materias_activas.append(m)
            
    if not materias_activas:
        print(">> No hay materias activas autorizadas por el Coordinador.")
    
    print("="*50)
    return materias_activas

def ofertar_materia(nombre_profesor):
    print("\n--- OFERTAR NUEVA SECCIÓN ---")

    disponibles = ver_materias_disponibles()
    if not disponibles:
        return

    codigo = input("\nIngrese el CÓDIGO de la materia a dictar: ").upper()
    
    materia_seleccionada = None
    for m in disponibles:
        if m["codigo_materia"] == codigo:
            materia_seleccionada = m
            break
    
    if not materia_seleccionada:
        print("Error: Código no válido o materia inactiva.")
        return

    print(f"\nSeleccionó: {materia_seleccionada['materia']}")
    seccion = input("Ingrese la Sección (ej. A, B, N1): ").upper()

    oferta_actual = cargar_datos(ARCHIVO_DB_PROFESOR)

    nueva_oferta = {
        "profesor": nombre_profesor,
        "codigo_materia": materia_seleccionada["codigo_materia"],
        "materia": materia_seleccionada["materia"],
        "seccion": seccion,
        "horario": [] 
    }
    
    oferta_actual.append(nueva_oferta)
    guardar_datos(ARCHIVO_DB_PROFESOR, oferta_actual)
    
    print(f"\n¡Sección {seccion} de {materia_seleccionada['materia']} creada exitosamente!")
    time.sleep(1.5)

def ver_mis_ofertas(nombre_profesor):
    todas_las_ofertas = cargar_datos(ARCHIVO_DB_PROFESOR)
    
    print(f"\n--- MATERIAS DICTADAS POR: {nombre_profesor.upper()} ---")
    encontrado = False
    
    for oferta in todas_las_ofertas:
        if oferta.get("profesor") == nombre_profesor: 
            print(f"• {oferta['materia']} (Sección {oferta['seccion']})")
            print(f"  Cupos: {oferta['cupo_disponible']} / {oferta['cupo_total']}")
            print("-" * 30)
            encontrado = True
    
    if not encontrado:
        print(">> Usted no ha ofertado materias todavía.")
    
    input("\nPresione Enter para volver...")



def menu_profesor(usuario_nombre):
    while True:

        if os.name == 'nt': os.system('cls')
        
        print(f"   PANEL DOCENTE: {usuario_nombre.upper()}")
        print("1. Ver Materias Activas (Catalogo General)")
        print("2. Ofertar Materia (Abrir Sección)")
        print("3. Ver mis secciones abiertas")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ver_materias_disponibles()
            input("\nPresione Enter para volver...")
            
        elif opcion == "2":
            ofertar_materia(usuario_nombre)
            
        elif opcion == "3":
            ver_mis_ofertas(usuario_nombre)
            
        elif opcion == "4":
            print("Cerrando sesión docente...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_profesor("PROFESOR_PRUEBA")