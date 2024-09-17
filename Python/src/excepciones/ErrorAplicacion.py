#Juan Miguel Ochoa/Sebastian Martinez/David Posada/Juan Diego Sanchez/Daniel Zambrano

class ErrorAplicacion(Exception):
    def __init__(self, error):
        self._error = "Manejo de errores de la Aplicación: " + error
    
    def mostrarMensaje(self):
        return self._error
      