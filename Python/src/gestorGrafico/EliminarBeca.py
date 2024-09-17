#Juan Miguel Ochoa/Sebastian Martinez/David Posada/Juan Diego Sanchez/Daniel Zambrano

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.FieldFrame import FieldFrame

class EliminarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#8B4513", highlightthickness=3, bg="#FAF3E0")  # Fondo beige claro
        self.pack(expand=True)

        def confEliminar():
            quest = messagebox.askokcancel("Confirmar acción", f"¿Está seguro que desea eliminar la beca {comboBecas.get()} del sistema?\n Esta acción será permanente.")
            if quest:
                bec = Beca.buscandoBeca(str(comboBecas.get()))
                try:
                    Beca.eliminarBeca(bec)
                    messagebox.showinfo("Beca eliminada", f"La beca {comboBecas.get()} ha sido eliminada con éxito del sistema")
                except:
                    messagebox.showerror("Error", "Debe seleccionar una beca del listado para poder continuar.")

        # Título de la ventana
        titulo = Label(self, text="Eliminar Beca", bg="#F5F5DC", fg="#8B4513", font=("Helvetica", 14, "bold"))  # Fondo beige claro, texto café oscuro
        titulo.pack(side="top", anchor="c")

        # Descripción
        textoDesc = ("A continuación, deberá seleccionar de la lista de becas existentes\n cuál de estas desea eliminar.")
        descripcion = Label(self, text=textoDesc, bg="#E7D3B1", font=("Arial", 11), fg="#8B4513")  # Fondo café claro, texto café oscuro
        descripcion.pack(anchor="n", pady=20)

        # Frame de la lista de becas
        becaFrame = Frame(self, bg="#E7D3B1")  # Fondo café claro
        becaFrame.pack()

        # Título del combo de becas
        becaTit = Label(becaFrame, text="Becas existentes", bg="#E7D3B1", font=("Arial", 11, "bold"), fg="#8B4513")  # Fondo café claro, texto café oscuro
        becaTit.grid(row=0, column=0, padx=10, pady=10)

        # Combo box para seleccionar la beca
        becasE = Beca.listaBecas()
        textoDefault = StringVar(becaFrame, value="Seleccione una beca")
        comboBecas = ttk.Combobox(becaFrame, values=becasE, textvariable=textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)

        # Botón de eliminar beca
        boton = Button(self, text="Eliminar Beca", command=confEliminar, font=("Arial", 11, "bold"), fg="#8B4513", bg="#E7D3B1")
        boton.pack(pady=10)