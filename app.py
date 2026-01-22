
def Dias_clases():
    dias = {
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"}        
horario_clases = [
    {
    "H1":"7:00 - 7:45",
    "H2":"7:45 - 8:30",
    "H3":"8:30 - 9:15",
    "H4":"9:15 - 10:00",
    "H5":"10:00 - 10:45",
    "H6":"10:45 - 11:30",
    "H7":"11:30 - 12:15",
    "H8":"12:15 - 13:00",
    }
]


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
    if not materia_encontrada:
        print("Código no encontrado en el catálogo.")
        return

    Dias_clases = input("Ingrese el día de la clase ej, Lunes: ")
    dia_encontrado = None
    for dia in Dias_clases:
        if dia in Dias_clases:
            dia_encontrado = dia
            print("Seleccionaste el día: " + dia)
            break
    if not dia_encontrado:
        print("Día inválido.")
        return
    
    cupo = int(input("Ingrese el cupo máximo de estudiantes:Ej, 30: "))
    if cupo < 50:
            print("Cupo establecido en: " + str(cupo))

    elif cupo <= 0:
            print("El cupo debe ser un número positivo.")

    elif cupo > 50:
            print("El cupo máximo permitido es 50.")
    
    bloques = input("Ingrese los bloques horarios")
    if horario_clases in horario_clases:
            print("Seleccionaste el bloque horario: " + horario_clases[horario_clases])
    else:
            print("Bloque horario inválido."+ horario_clases[horario_clases])
            return
    
    seccion = input("Ingrese la sección de la materia: ")
    if seccion is oferta_materias:
            print("Seleccionaste la seccion"+ oferta_materias[seccion])
            return
    
    activa = input("¿La materia está activa? (True/False): ").lower() == 'true'
crearoferta_materias()
#rehice todo el codigo porque estaba mal estructurado y con errores aparte se me olvido que queria hacer.
#teoricamente ya funciona, lee perono guarda nada aun.