# Juan Diego Sanchez / Daniel Hernando Zambrano Gonzales/ David Posada Salazar/ Juan Miguel Ochoa Agudelo/ Sebastian Martinez Sequeira

class Horario:
    horarios_totales = []  # Lista estática para almacenar todos los horarios

    def __init__(self, dia_semana=None, hora_inicio=None, hora_final=None, grupo=None, horario_clases=None):
        # Matriz 7x24 para representar los días y horas
        self.horario = [[None for _ in range(24)] for _ in range(7)]
        self.grupo_contenidos = []
        
        if horario_clases is not None and grupo is not None:
            # Constructor que recibe lista de clases como strings
            self.grupo_contenidos.append(grupo)
            for clase in horario_clases:
                dia = int(clase[:1]) - 1
                hora_inicio = int(clase[2:4])
                hora_final = int(clase[5:7])
                for hora in range(hora_inicio, hora_final):
                    self.horario[dia][hora] = grupo
        elif dia_semana is not None and hora_inicio is not None and hora_final is not None and grupo is not None:
            # Constructor que recibe el día, hora de inicio, hora final y grupo
            self.grupo_contenidos.append(grupo)
            for hora in range(hora_inicio, hora_final):
                self.horario[dia_semana][hora] = grupo
        else:
            # Constructor por defecto
            Horario.horarios_totales.append(self)

    def ocupar_horario(self, horario_clases, grupo):
        # Método para ocupar el horario basado en una lista de clases como strings
        self.grupo_contenidos.append(grupo)
        for clase in horario_clases:
            dia = int(clase[:1]) - 1
            hora_inicio = int(clase[2:4])
            hora_final = int(clase[5:7])
            for hora in range(hora_inicio, hora_final):
                self.horario[dia][hora] = grupo

    def __str__(self):
        # Método para representar el horario en formato tabla
        horario_str = "HORA        LUNES        MARTES        MIERCOLES        JUEVES        VIERNES        SABADO        DOMINGO\n"
        for i in range(24):
            if i < 9:
                hora_str = f"0{i}-0{i+1}       "
            else:
                hora_str = f"{i}-{i+1}       "

            fila = [hora_str]
            for j in range(7):
                if self.horario[j][i] is None:
                    materia = ""
                else:
                    materia = self.horario[j][i].get_materia().get_abreviatura()
                fila.append(materia.ljust(12))
            horario_str += ''.join(fila) + "\n"
        return horario_str

    @classmethod
    def get_horarios_totales(cls):
        return cls.horarios_totales

    def get_grupo_contenidos(self):
        return self.grupo_contenidos

    def set_grupo_contenidos(self, grupo_contenidos):
        self.grupo_contenidos = grupo_contenidos
