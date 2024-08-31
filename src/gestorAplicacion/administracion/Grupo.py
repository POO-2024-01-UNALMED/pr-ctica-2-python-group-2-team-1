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
        
    def mostrar_informacion_grupo(self):
        retorno = f'Número del grupo: {self.numero}, Profesor: {self.profesor}, Horario: {self.horario}, Cupos: {self.cupos}, Salon: {self.salon}'
        return retorno
    
    def existencia_estudiante(self, estudiante):
        for est in self.estudiantes:
            if est.get_id() == estudiante.get_id():
                return True
        return False
    
    def eliminar_estudiante(self, estudiante):
        indice = -1
        for i, est in enumerate(self.estudiante):
            if est.get_nombre() == estudiante.get_nombre():
                indice = i
                self.cupos += 1
                estudiante.eliminar_grupo(self)
                break
        if indice != -1:
            self.estudiantes.pop(indice)