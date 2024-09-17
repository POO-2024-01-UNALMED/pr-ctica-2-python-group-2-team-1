from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import os
from excepciones.ErrorManejo import *
from gestorAplicacion.administracion.Materia import Materia

class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#8B5A2B", highlightthickness=3, background="#F5E6C4")  # Marrón oscuro
        self.pack(expand=True)

        # Configuración del estilo para Combobox
        style = ttk.Style()
        style.configure("TCombobox", fieldbackground="#F5D5B0", background="#F5E6C4", foreground="#8B5A2B")  # Fondo crema claro y texto marrón oscuro

        def botEliminar():
            confirmacion = messagebox.askokcancel("Confirmación de eliminación", "¿Está seguro que desea eliminar el grupo {} de la materia {}?".format(entGrupo.get(), box.get()))
            if confirmacion:
                try:
                    mate = Materia.encontrarMateria(str(box.get()))
                    mate.eliminarGrupo(int(entGrupo.get()))
                    messagebox.showinfo("Grupo eliminado", "El grupo ha sido eliminado con éxito de la materia")
                except:
                    messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

        def limpiar():
            box.delete(0, END)
            entGrupo.delete(0, END)

        # Título de la ventana con fondo marrón oscuro y texto en color crema
        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14), fg="#F5E6C4", bg="#8B5A2B")
        titulo.pack(side="top", anchor="c", padx=5, pady=5)

        # Descripción con fondo marrón oscuro y texto en color crema
        texto = "A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada."
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="#F5E6C4", bg="#8B5A2B")
        descripcion.pack(anchor="n", pady=20, padx=5)

        # Subframe con fondo crema claro
        subFrame = Frame(self, bg="#F5E6C4")  
        subFrame.pack(padx=5, pady=5)

        # Encabezados de columnas con fondo marrón oscuro y texto en color crema
        tituloC = Label(subFrame, text="Criterio", font=("Arial", 11), fg="#F5E6C4", bg="#8B5A2B")
        tituloC.grid(row=0, column=0, padx=10, pady=8)

        tituloV = Label(subFrame, text="Valor", font=("Arial", 11), fg="#F5E6C4", bg="#8B5A2B")
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        textoM = Label(subFrame, text="Materia", font=("Arial", 11), fg="#F5E6C4", bg="#8B5A2B")
        textoM.grid(row=1, column=0, padx=10, pady=8)

        # Combobox con las materias usando el estilo configurado
        valores = Materia.listaNombresMaterias()
        box = ttk.Combobox(subFrame, values=valores, font=("Arial", 10), style="TCombobox")
        box.grid(row=1, column=1, padx=10, pady=8)

        textoM = Label(subFrame, text="Grupo", font=("Arial", 11), fg="#F5E6C4", bg="#8B5A2B")
        textoM.grid(row=2, column=0, padx=10, pady=8)

        # Entrada de texto para el grupo
        entGrupo = Entry(subFrame, font=("Arial", 11))
        entGrupo.grid(row=2, column=1, padx=10, pady=8)

        # Botones con fondo crema claro y texto marrón oscuro
        botonEliminar = Button(subFrame, text="Eliminar", command=botEliminar, font=("Arial", 11), fg="#8B5A2B", bg="#F5D5B0")
        botonEliminar.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        botonLimpiar = Button(subFrame, text="Limpiar", command=limpiar, font=("Arial", 11), fg="#8B5A2B", bg="#F5D5B0")
        botonLimpiar.grid(row=3, column=1, padx=10, pady=10)
