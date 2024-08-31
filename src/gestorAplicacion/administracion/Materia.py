import gestorAplicacion.administracion
from gestorAplicacion.usuario import *

class Materia:
    materiasTotales = []
    def __init__(self, nombre, codigo, descripcion, creditos, facultad, cupos,abreviatura):
        self._nombre = nombre
        self._codigo = codigo
        self._descripcion = descripcion
        self._creditos = creditos
        self._facultad = facultad
        self._cupos = cupos
        self._prerrequisitos = []
        self._grupos = []
        self._abreviatura = abreviatura
        
        Materia.materiasTotales.append(self)
        
    #Metodos
    def cantidadCupos(self):
        cantidad = 0
        for grupo in self.getGrupos():
            cantidad += grupo.getCupos()
        return cantidad
    
    #Este es un metodo de instacia el cual crea nuevos grupos con los parametros que se proporcionen.
    #Devolviendo asi el grupo generado.
    
    def crearGrupo(self, numero, profesor, horario, cupos, salon):
        grupo = Grupo(self, numero, profesor, horario, cupos, salon)
        self.cantidadCupos()
        self.grupos.append(grupo)
        return grupo 
    
    #Este metodo muestra más informacion acerca de la materia
    def mostrarContenidos(self):
        contenido = f"Materia: {self._nombre}, 
                    \nCodigo: {self._codigo},
                    \nCreditos: {self._creditos},
                    \nFacultad: {self._facultad},
                    \nDescripcion: \n {self._descripcion}" #Esto deberia de funcionar, supongo.
        return contenido  
    
    #Este metodo afirma si existe el grupo que se busca
    def existenciaGrupo(self, grupoBuscado):
        if self.grupos: #Para usar algo similar a 'isEmpty' usamos self para verificar si la lista existe.
            for grupo in self.grupos:
                if grupo == grupoBuscado:
                    return True
            return False
        else:
            return False

    #Metodos utilizados para eliminar y agregar un grupo paso por paso
    def eliminarGrupo(self, numero):
        grupo = self._grupos[numero - 1]
        grupo.getProfesor().desvincularGrupo(grupo)
        grupo.getSalon().getHorario().liberarHorario(grupo.getHorario)
        self.grupos.remove(grupo)
        self._cupos -= grupo.getCupos()
        for i in range(numero - 1, len(self._grupos)):
            grupoCamb = self.grupos[i]
            nGrupoAnt = grupoCamb.getNumero()
            grupoCamb.setNumero(nGrupoAnt - 1)
            
    def agregarGrupo(self, numero, profesor, horario, cupos, salon):
        
        #El método recibe los parámetros necesarios para crear un nuevo grupo
        dispSalon = True
        dispProfesor = True
        daMateria = profesor.daMateria(self._nombre)
        
        #Se comprueba la disponibilidad del profesor y el salón para el horario ingresado. 
        #Si al menos uno no se cumple, no se agrega el grupo
        for hor in horario:
            dispProfesor = profesor.getHorario().comprobarDisponibilidad[hor]
            dispSalon = salon.getHorario().comprobarDisponibilidad[hor]
            
            if not dispProfesor or not dispSalon:
                break
        
        #En caso de contar con disponibilidad, se procede a declarar el nuevo grupo y 
        #agregárselo a su respectiva materia, profesor y salón
        if dispProfesor and dispSalon and daMateria:
            nGrupo = self.crearGrupo(self, numero, profesor, horario, cupos, salon)
            self._cupos += cupos
            salon.getHorario().ocuparHorario(self, horario, nGrupo) 
            profesor.vincularGrupo(self, nGrupo)  
    
    #Metodo que retorna el grupo de un estudiante en especifico
    def buscarGrupoDeEstudiante(self, estudiante):
        for grupo in self._grupos:
            for e in grupo.getEstudiantes():
                if e == estudiante:
                    return grupo
        return None
    
    #Busca una materia, teniendo en cuenta su nombre y su codigo.
    #Si no existe, retorna -1
    @staticmethod
    def buscarMateria(self, nombre, codigo):
        for i, materia in enumerate(Materia.materiasTotales):
            if materia.getNombre() == nombre and materia.getCodigo() == codigo:
                return i
        return -1
    
    #Comprueba si un estudiante puede estar en un grupo, dependiendo de los cupos, creditos, prerrequisitos y disponibilidad
    @staticmethod
    def puedeVerMateria(self, estudiante, grupo):
        
        if not (estudiante.getCreditos() + grupo.getMateria().getCreditos() <= self.Coordinador.getLimitesCreaditos):
            return False
        
        if not estudiante.getHorario().comprobarDisponibilidad(grupo.getHorario):
            return False
        
        if grupo.getCupos() == 0:
            return False
        
        if not self.comprobarPrerrequisitos(estudiante, grupo.getMateria()):
            return False
        
        return True
    
    @staticmethod
    def comprobarPrerrequisitos(self, estudiante, materia):
        materiasVistas = []
        for pGrupo in estudiante.getGruposVistos():
            materiasVistas.append(pGrupo.getMateria())
        
        for pMateria in materia.getPrerrequisitos():
            flag = False
            for pVistas in materiasVistas:
                if pMateria.getCodigo() == pVistas.getCodigo():
                    flag = True
                    break
            
            if not flag:
                return False
        
        return True
    
    