from typing import List

class Materia:
    def __init__(self, nombre:str, creditos:str):  # constructor
        self.nombre = nombre
        self.creditos = creditos
        self.calificacion = ""

class Estudiante:
    def __init__(self, nombre: str, id: str, carrera: str,materias: List[Materia], indice_acu:str, puntos_acumu:str,
                 creditos_acu:str, creditos_cursando:str, cant_materias_curso: int):
        self.nombre = nombre
        self.id = id
        self.correo = str(id + "@ce.pucmm.edu.do")
        self.carrera = carrera
        self.materias = materias
        self.indice_acu = indice_acu
        self.puntos_acumu = puntos_acumu
        self.creditos_acu = creditos_acu
        self.creditos_cursando = creditos_cursando
        self.cant_materias_curso = cant_materias_curso