class Salon:
    salones = []  # Lista estática para almacenar todos los salones

    def __init__(self, lugar, aforo):
        self.lugar = lugar
        self.aforo = aforo
        self.horario = horario()  # Asumimos que la clase Horario está definida en algún lugar
        Salon.salones.append(self)

    @staticmethod
    def mostrar_salones():
        # Método estático para mostrar los salones
        retorno = ""
        for i, salon in enumerate(Salon.salones, start=1):
            retorno += f"{i}. {salon.lugar}.\n"
        return retorno

    # Métodos getter y setter
    def get_lugar(self):
        return self.lugar

    def set_lugar(self, lugar):
        self.lugar = lugar

    def get_aforo(self):
        return self.aforo

    def set_aforo(self, aforo):
        self.aforo = aforo

    def get_horario(self):
        return self.horario

    def set_horario(self, horario):
        self.horario = horario

    @staticmethod
    def get_salones():
        return Salon.salones

    @staticmethod
    def set_salones(salones):
        Salon.salones = salones