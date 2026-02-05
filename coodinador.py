import json
from os import path

ARCHIVO_JSON = "materias.json"
ARCHIVO_USUARIOS = "usuarios.json"

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

# --- FUNCIONES DE USUARIOS ---
def cargar_usuarios_db():
    if path.exists(ARCHIVO_USUARIOS):
        try:
            with open(ARCHIVO_USUARIOS, "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_usuarios_db(lista_usuarios):
    with open(ARCHIVO_USUARIOS, "w", encoding='utf-8') as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)

def ver_lista_usuarios():
    usuarios = cargar_usuarios_db()
    print("\n" + "="*50)
    print(f"{'USUARIO (CEDULA)':<20} | {'ROL ACTUAL'}")
    print("="*50)
    for u in usuarios:
        print(f"{u['usuario']:<20} | {u['rol'].upper()}")
    print("="*50)
    return usuarios

def cambiar_jerarquia():
    print("\n--- CAMBIAR ROL DE USUARIO ---")
    usuarios = ver_lista_usuarios() 
    
    usuario_buscado = input("\nIngrese el USUARIO (Cédula) a modificar: ").strip()
    
    usuario_encontrado = None
    for u in usuarios:
        if u["usuario"] == usuario_buscado:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Usuario no encontrado.")
        return

    print(f"\nUsuario seleccionado: {usuario_encontrado['usuario']}")
    print(f"Rol actual: {usuario_encontrado['rol'].upper()}")
    
    print("\nSeleccione el NUEVO rol:")
    print("1. Coordinador")
    print("2. Profesor")
    print("3. Alumno")
    
    op = input("Opción: ")
    nuevo_rol = ""
    
    if op == "1": nuevo_rol = "coordinador"
    elif op == "2": nuevo_rol = "profesor"
    elif op == "3": nuevo_rol = "alumno"
    else:
        print("⛔ Opción inválida.")
        return

    # Guardamos el cambio
    usuario_encontrado["rol"] = nuevo_rol
    guardar_usuarios_db(usuarios)
    print(f"✅ ¡Cambio exitoso! Ahora {usuario_encontrado['usuario']} es {nuevo_rol.upper()}.")

# --- FUNCIONES DE MATERIAS ---

def mostrar_todas(lista_materias):
    print("\n--- LISTA DE MATERIAS ---")
    for m in lista_materias:
        estado = "ACTIVA" if m['activa'] else "INACTIVA"
        uc_actual = m.get('uc', 3)
        print(f"[{m['codigo_materia']}] {m['materia']} ({uc_actual} UC) - Cupo: {m['cupo']} - Estado: {estado}")

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

    uc_actual = materia_encontrada.get('uc', 3)

    print(f"\nEditando: {materia_encontrada['materia']}")
    print(f"Estado actual: {'Activa' if materia_encontrada['activa'] else 'Inactiva'}")
    print(f"Cupo actual: {materia_encontrada['cupo']}")
    print(f"UC actuales: {uc_actual}")
    
    print("\n¿Qué desea hacer?")
    print("A. Activar/Desactivar materia")
    print("B. Modificar Cupo")
    print("C. Modificar Unidades de Crédito (UC)")
    print("D. Cancelar")
    
    accion = input("Elija una opción: ").upper()
    hay_cambios = False

    if accion == "A":
        estado_nuevo = not materia_encontrada['activa']
        materia_encontrada['activa'] = estado_nuevo
        print(f"Estado cambiado a: {estado_nuevo}")
        hay_cambios = True

    elif accion == "B":
        try:
            nuevo_cupo = int(input("Ingrese nuevo cupo: "))
            materia_encontrada['cupo'] = nuevo_cupo
            hay_cambios = True
        except ValueError:
             print("Error: Ingrese solo números.")

    elif accion == "C": 
        try:
            nueva_uc_val = int(input("Ingrese nuevas UC: "))
            materia_encontrada['uc'] = nueva_uc_val
            hay_cambios = True
        except ValueError:
            print("Error: Debe ingresar un número.")
        
    elif accion == "D":
        print("Operación cancelada.")
        
    if hay_cambios:
        guardar_datos(lista_materias)

# --- MENÚ PRINCIPAL ---

def menu_coordinador():
    # Cargamos las materias al inicio del ciclo
    materias = cargar_datos()
    
    while True:
        print("\n--- SISTEMA COORDINADOR UNEFA ---")
        print("1. Buscar y Modificar Materia")
        print("2. Ver todas las materias")
        print("3. Crear Nueva Materia")
        print("4. Cambiar Jerarquía de Usuario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_y_modificar(materias)
        
        elif opcion == "2":
            mostrar_todas(materias)

        elif opcion == "3":
            # --- AQUÍ ESTABA EL ERROR: TODO ESTO ESTABA AFUERA ---
            print("\n--- CREAR NUEVA MATERIA ---")
            
            # 1. Pedir y Validar Código
            nuevo_codigo = input("Ingrese el CÓDIGO (ej. MAT0202): ").upper()
            
            codigo_existe = False
            for m in materias:
                if m["codigo_materia"] == nuevo_codigo:
                    codigo_existe = True
                    break
            
            if codigo_existe:
                print("¡Error! Ya existe una materia con ese código.")
            else:
                # 2. Pedir resto de datos
                nuevo_nombre = input("Nombre de la materia: ")
                
                # Validación de cupo
                nuevo_cupo = 0
                while True:
                    entrada_cupo = input("Ingrese cupo máximo (numérico): ")
                    if entrada_cupo.isdigit():
                        nuevo_cupo = int(entrada_cupo)
                        break
                    else:
                        print("Por favor, ingrese un número válido.")

                # Validación de UC
                nuevas_uc = 0
                while True:
                    entrada_uc = input("Ingrese Unidades de Crédito (ej. 3): ")
                    if entrada_uc.isdigit():
                        nuevas_uc = int(entrada_uc)
                        break
                    else:
                        print("Por favor, ingrese un número válido para las UC.")

                dia_input = input("Día de clase (ej. Lunes): ").capitalize()
                
                print("Bloques: 0=7:00, 1=7:45, 2=8:30, 3=9:15, 4=10:00...")
                bloques_str = input("Ingrese bloques separados por coma (ej. 0,1): ")
                
                lista_bloques = []
                if bloques_str: 
                    partes = bloques_str.split(",")
                    for p in partes:
                        if p.strip().isdigit():
                            lista_bloques.append(int(p.strip()))

                # 3. Crear el diccionario
                nueva_materia = {
                    "codigo_materia": nuevo_codigo,
                    "materia": nuevo_nombre,
                    "uc": nuevas_uc,
                    "dia": [dia_input],
                    "cupo": nuevo_cupo,
                    "bloques": lista_bloques,
                    "seccion": "D1",        
                    "activa": True          
                }
                
                # 4. Agregar y Guardar
                materias.append(nueva_materia)
                guardar_datos(materias)
                print(f"\n>>> ¡Materia '{nuevo_nombre}' ({nuevas_uc} UC) creada exitosamente!")

        elif opcion == "4":
            cambiar_jerarquia()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_coordinador()
