import os
import json
import time

import alumno
import coodinador
import profesor

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

os.chdir(carpeta_actual)

if __name__ == "__main__":

    usuarios_db = {}
    if os.path.exists("usuarios.json"):
        try:
            with open("usuarios.json", 'r', encoding='utf-8') as archivo:
                usuarios_db = json.load(archivo)
        except:
            print("Error: No se pudo leer usuarios.json")
            usuarios_db = {}
    else:
        print("Advertencia: No existe el archivo usuarios.json en la carpeta actual.")

    while True:

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("=========================================")
        print("   SISTEMA DE GESTIÓN UNEFA - 2026")
        print("=========================================")
        print("1. Coordinador")
        print("2. Alumno")
        print("3. Profesor")
        print("4. Salir")
        print("=========================================")
        
        opcion_rol = input("Seleccione su perfil (1-4): ")

        if opcion_rol == "4":
            print("Cerrando sistema... ¡Hasta luego!")
            break

        rol_esperado = ""
        if opcion_rol == "1":
            rol_esperado = "coordinador"
        elif opcion_rol == "2":
            rol_esperado = "alumno"
        elif opcion_rol == "3":
            rol_esperado = "profesor"
        else:
            input("Opción no válida. Presione Enter para intentar de nuevo...")
            continue 

        print(f"\n--- INGRESO: {rol_esperado.upper()} ---")

        prefijo_doc = ""
        while True:
            tipo_input = input("Tipo de Documento (V/E/P) [o 'A' para Admin]: ").upper()
            if tipo_input in ["V", "E", "P"]:
                prefijo_doc = tipo_input
                break
            elif tipo_input == "A":
                prefijo_doc = "ADMIN"
                break
            else:
                print("Error: Debe escribir V, E o P.")

        usuario_ingresado = input("Ingrese Cédula/Pasaporte: ")
        clave_ingresada = input("Ingrese Contraseña: ")

        usuario_valido = False
        datos_usuario = None

        if prefijo_doc == "ADMIN":
      
            usuario_busqueda = usuario_ingresado 
        else:
        
            usuario_busqueda = f"{prefijo_doc}-{usuario_ingresado}"

        datos_usuario = None
        
        for u in usuarios_db:

            if u.get("usuario") == usuario_busqueda:
                datos_usuario = u
                break  
        if datos_usuario:
            if datos_usuario["clave"] == clave_ingresada:
                if datos_usuario["rol"] == rol_esperado:
                    usuario_valido = True
                else:
                    print(f"\nError: Este usuario no tiene permisos de {rol_esperado}.")
            else:
                print("\nError: Contraseña incorrecta.")
        else:
            print(f"\nError: Usuario '{usuario_busqueda}' no encontrado.")
            if prefijo_doc != "ADMIN":
                print(f"(El sistema buscó '{usuario_busqueda}'. Verifique V/E/P)")

        if usuario_valido:
            print(f"\n¡Bienvenido, usuario {usuario_busqueda}!") 
            time.sleep(1.5) 

            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            if rol_esperado == "coordinador":
                coodinador.menu_coordinador()
            
            elif rol_esperado == "alumno":

                alumno.menu_alumno(usuario_busqueda)
                
            elif rol_esperado == "profesor":
                profesor.menu_profesor(usuario_busqueda)
        
        else:

            input("\nPresione Enter para volver a intentar...")