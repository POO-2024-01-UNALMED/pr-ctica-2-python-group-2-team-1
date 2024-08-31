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
    
    