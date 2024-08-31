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
            #Enumerate usado para obtener tanto el indice como el valor de cada elemento
            if est.get_nombre() == estudiante.get_nombre():
                indice = i
                self.cupos += 1
                estudiante.eliminar_grupo(self)
                break
        if indice != -1:
            self.estudiantes.pop(indice)
    
    @staticmethod
    def buscar_grupo(materiaE, grupoE):
        indicei = -1
        indicej = -1

        for i, materia in enumerate(Materia.get_materias_totales()):
            if materia.get_nombre() == materiaE.get_nombre():
                indicei = i
                
                for j, grupo in enumerate(materia.get_grupos()):
                    if grupo.get_numero() == grupoE.get_numero():
                        indice = j
                        break
                break
        
        return Materia.get_materias_totales()[indicei].get_grupos()[indicej]
    
    def agregar_estudiantes(self, estudiante):
        self.estudiantes.append(estudiante)
        self.cupos -= 1
        
    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero): 
	    self.numero = numero
    
    def setProfesor(self, profesor):
        self.profesor = profesor
    
    def getHorario(self):
        return self.horario
    
    def setHorario(self, horario):
        self.horario = horario
    
    def getCupos(self):
        return self.cupos
    
    def setCupos(self, cupos):
        self.cupos = cupos
    
    def getSalon(self):
        return self.salon
    
    def setSalon(self, salon):
        self.salon = salon
    
    def getEstudiantes(self):
        return self.estudiantes
    
    def setEstudiantes(self, estudiantes):
        self.estudiantes = estudiantes
        
    def getMateria(self):
        return self.materia
    
    def setMateria(self, materia):
        self.materia = materia
    
    @staticmethod
    def getGruposTotales():
        return Grupo.grupos_totales