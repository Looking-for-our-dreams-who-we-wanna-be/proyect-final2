def horario(bloquesdia):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    horario_completo = {}

    length = len(bloquesdia)
    for i in range(length):
        horario_completo[dias[i]] = bloquesdia[i]

    return horario_completo
def horas(bloqueshora):
    horas_bloques = [ "7:00-7:45", "7:45-8:30", "8:30-9:15", "9:15-10:00", "10:00-10:45", "10:45-11:30",
                      "11:30-12:15", "12:15-13:00"] 
    lista_traducida = []

    for numero in bloqueshora:
        indice = numero - 1  # Ajustar para índice basado en cero
        if 0 <= indice < len(horas_bloques):
            texto_hora = horas_bloques[indice]
            lista_traducida.append(texto_hora)           
    return lista_traducida

oferta_materias = {
    "codigo_materia": "01S-MAT0101",
    "materia": "Matematicas I", 
    "dia": [0 , 3],
    "cupo" : 30,
    "bloques": [0, 1, 2, 3, 4],
    "seccion": "D1",
}
{
    "codigo_materia": "01S-FIS0101",
    "materia": "Fisica I",
    "dia": [1, 4],
    "cupo" : 30,
    "bloques": [3, 4],
    "seccion": "D1",
}
{
    "materia": "Quimica I",
    "codigo_materia": "01S-QUI0101",
    "dia": [2, 5],
    "cupo" : 30,
    "bloques": [1, 2, 3],
    "seccion": "D1",
}
{
    "01S-LOG0101": "Geometría analítica",
    }
# faltan materias juasjuas de mientras esta asi pero hay que completarlocon el mismo formato
