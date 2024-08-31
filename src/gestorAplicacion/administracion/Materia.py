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
        
        
        