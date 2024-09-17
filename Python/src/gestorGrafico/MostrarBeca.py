from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.MatricularMateria import MatricularMateria
from gestorGrafico.FieldFrame import FieldFrame

class MostrarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#F5F5DC")

        def mosBeca():
            infoBecas = ""
            i = 1
            for beca in Beca.getBecas():
                a = beca.getConvenio() 
                infoBecas += f"{str(i)}. {str(a)}.\n    Cupos disponibles: {beca.getCupos()}\n    Estrato máximo para acceder: {beca.getEstratoMinimo()}.\n    Créditos inscritos requeridos: {beca.getCreditosInscritosRequeridos()}.\n    Ayuda económica: {str(beca.getAyudaEconomica())}.\n\n"
                i += 1
            return infoBecas

        tituloenventana = Label(self, text="Mostrar Becas Existentes", bg="#8B4513", fg="white", font=("Helvetica", 14, "bold"))
        tituloenventana.pack(side="top", anchor="c", padx=5, pady=5)
        textodescriptivo = "A continuación puede conocer información básica sobre las becas activas actualmente."
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 11), bg="#F5F5DC", fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        contenedor = Frame(self, bg="#F5F5DC")
        contenedor.pack() 

        lista = Text(contenedor, borderwidth=0, font=("Arial", 11))
        lista.pack()
        lista.configure(height=35)
        text = mosBeca()
        MatricularMateria.mostrar_texto(text, lista)