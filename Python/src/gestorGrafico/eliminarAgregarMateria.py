#Juan Miguel Ochoa

from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.agregarMateria import agregarMateria
from gestorGrafico.eliminarMateria import eliminarMateria
from gestorGrafico.agregarGrupo import agregarGrupo
from gestorGrafico.eliminarGrupo import eliminarGrupo

class EliminarAgregarMateria(Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#8B4513", highlightthickness=3, bg="#F5F5DC")
        self.pack(expand=True)

        def agMateria():
            self.pack_forget()
            agM = agregarMateria(ventana)
            agM.pack()

        def elMateria():
            self.pack_forget()
            elM = eliminarMateria(ventana)
            elM.pack()

        def agGrupo():
            self.pack_forget()
            agG = agregarGrupo(ventana)
            agG.pack()

        def elGrupo():
            self.pack_forget()
            elM = eliminarGrupo(ventana)
            elM.pack()

        titulo = Label(self, text="Agregar/Eliminar Materia/Grupo", font=("Arial", 14), fg="#8B4513", bg="#F5F5DC")
        titulo.pack(side="top", anchor="c", padx=5, pady=5)

        texto = ("Esta funcionalidad permite:\n1. Agregar una nueva materia al sistema. 3. Agregar un grupo a una materia existente."+
                 "\n2. Eliminar una materia existente del sistema. 4. Eliminar un grupo existente en alguna materia.")
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="#8B4513", bg="#F5F5DC")
        descripcion.pack(anchor="n", pady=20, padx=5)

        opciones = Frame(self, bg="#F5F5DC")
        opciones.pack(padx=5, pady=5)

        agMat = Button(opciones, text="Agregar Materia", font=("Arial", 11), command=agMateria, fg="#8B4513", bg="#D2B48C")
        agMat.pack(padx=20, pady=10)
        elMat = Button(opciones, text="Eliminar Materia", font=("Arial", 11), command=elMateria, fg="#8B4513", bg="#D2B48C")
        elMat.pack(padx=20, pady=10)
        agGrup = Button(opciones, text="Agregar Grupo", font=("Arial", 11), command=agGrupo, fg="#8B4513", bg="#D2B48C")
        agGrup.pack(padx=20, pady=10)
        elGrup = Button(opciones, text="Eliminar Grupo", font=("Arial", 11), command=elGrupo, fg="#8B4513", bg="#D2B48C")
        elGrup.pack(padx=20, pady=10)

#vent = Tk()
#vent.title("Szs")
#vent.geometry("600x350")

#eliminarAgregarMateria(vent).pack()
#vent.mainloop()
