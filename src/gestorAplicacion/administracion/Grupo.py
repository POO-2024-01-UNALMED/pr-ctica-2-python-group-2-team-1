import gestorAplicacion.administracion
from gestorAplicacion.usuario import *

class Grupo:
    grupos_totales = []
    
    def __init__(self, materia, numero, profesor, horario = None, cupos = None, salon = None):
        self.materia = materia
        self.numero = numero
        self.profesor = profesor
        self.horario = horario if horario is not None else []
        self.cupos = cupos
        self.salon = salon
        self.estudiantes = []
        Grupo.grupos_totales.append(self)