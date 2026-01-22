
dias = {
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"}        
bhoras = {
        0:"7:00 - 7:45",
        1:"7:45 - 8:30",
        2:"8:30 - 9:15",
        3:"9:15 - 10:00",
        4:"10:00 - 10:45",
        5:"10:45 - 11:30",
        6:"11:30 - 12:15",
        7:"12:15 - 13:00"
        }

oferta_materias = [
{
    "codigo_materia": "MAT0101",
    "materia": "Matematicas I", 
    "dia": "",
    "cupo" : 0,
    "bloques": [],
    "seccion": "",
    "horario": "",
    "activa": False,
},
{
    "codigo_materia": "FIS0101",
    "materia": "Fisica I",
    "dia": [],
    "cupo" : 0,
    "bloques": [],
    "seccion": "D1",
    "activa": False,
},
{
    "materia": "Quimica I",
    "codigo_materia": "QUI0101",
    "dia": [],
    "cupo" : 0,
    "bloques": [],
    "seccion": "D1",
    "activa": False,
},
{
    "01S-LOG0101": "Geometría analítica",
    },
]

# faltan materias juasjuas de mientras esta asi pero hay que completarlocon el mismo formato

def crearoferta_materias():
    print ("Crear oferta de materias")
    
    codigo = input("Ingrese el código de la materia: ")
    materia_encontrada = None
    for materia in oferta_materias:
        if materia["codigo_materia"] == codigo:
            materia_encontrada = materia
            print("Usted elegio la materia: " + materia["materia"])
            break
        elif materia["materia"] == codigo:
            materia_encontrada = materia
            print("Usted elegio la materia: " + materia["materia"])
            break
    if not materia_encontrada:
        print("Código no encontrado en el catálogo.")
        return

    Dias_clases = input("Ingrese el día de la clase ej, Lunes: ")
    dia_encontrado = None
    for dia in Dias_clases:
        if dia in Dias_clases:
            dia_encontrado = dia
            print("Seleccionaste el día: " + dia_encontrado)
            break
    if not dia_encontrado:
        print("Día inválido.")
        return
    
    cupo = int(input("Ingrese el cupo máximo de estudiantes, máximo 50: "))
    if cupo < 50:
            print("Cupo establecido en: " + str(cupo))

    elif cupo <= 0:
            print("El cupo debe ser un número positivo.")

    elif cupo > 50:
            print("El cupo máximo permitido es 50.")

    Horas_clases = input("Ingrese los bloques horarios: ")
    horario_encontrado = None
    for horas in bhoras:
        if horas in bhoras:
            horario_encontrado = bhoras[horas]
            print("Seleccionaste el bloque horario: " + horario_encontrado)
            break
        if not horario_encontrado:
            print("Bloque horario inválido.")
            return
    
    seccion = input("Ingrese la sección de la materia: ")
    if seccion is oferta_materias:
            print("Seleccionaste la seccion"+ oferta_materias[seccion])
            return


crearoferta_materias()
#rehice todo el codigo porque estaba mal estructurado y con errores aparte se me olvido que queria hacer.
#teoricamente ya funciona, lee perono guarda nada aun.