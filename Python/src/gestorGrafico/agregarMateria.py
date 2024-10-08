#Juan Miguel Ochoa/Sebastian Martinez/David Posada/Juan Diego Sanchez/Daniel Zambrano
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#D2B48C", highlightthickness=3, bg= "#F5F5DC")  # Tono intermedio de café
        self.pack(expand=True)

        def limpiar1():
            nombreE.delete(0, last=END)
            codigoE.delete(0, last=END)
            descripcionE.delete(0, last=END)
            creditosE.delete(0, last=END)
            prerrequisitosE.delete(0, last=END)
            facuE.delete(0, last=END)

        def siguiente():
            try:
                nombre = nombreE.get()
                codigo = int(codigoE.get())
                descripcion = descripcionE.get()
                creditos = int(creditosE.get())
                nPrer = int(prerrequisitosE.get())
                if nPrer < 0 or nPrer > 5:
                    raise CampoInvalido()
                prerrequisitos = []
                facultad = facuE.get()

                if nPrer > 0:
                    boxes = []
                    sFrame.pack_forget()

                    subFrame = Frame(self, bg="#F5F5DC")  # Fondo claro de tonalidad café
                    subFrame.pack()
                    tituloC = Label(subFrame, text="Criterio", font=("Arial", 11), fg="#8B4513", bg="#D2B48C", padx=5, pady=5)
                    tituloC.grid(row=0, column=0, padx=10, pady=8)

                    tituloV = Label(subFrame, text="Materia", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
                    tituloV.grid(row=0, column=1, padx=10, pady=8)
                    for i in range(nPrer):
                        lCriterio = Label(subFrame, text="Prerrequisito {}".format(str(i+1)), font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
                        lCriterio.grid(row=i+1, column=0, padx=10, pady=8)

                        valores = Materia.listaNombresMaterias()
                        prer = ttk.Combobox(subFrame, values=valores, font=("Arial", 11))
                        prer.grid(row=i+1, column=1, padx=10, pady=8)
                        boxes.append(prer)

                    def finalizarP():
                        confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                        if confirmacion:
                            try:
                                for box in boxes:
                                    if not isinstance(Materia.encontrarMateria(box.get()), Materia):
                                        raise CampoVacio()
                                Coordinador.getUsuarioIngresado().agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                                messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")
                            except:
                                messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

                    def limpiar2():
                        for box in boxes:
                            box.delete(0, last=END)

                    bAgregar = Button(subFrame, text="Agregar materia", command=finalizarP, font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
                    bAgregar.grid(row=len(boxes)+1, column=0, padx=10, pady=10, sticky='e')

                    bLimpiar = Button(subFrame, text="Limpiar", command=limpiar2, font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
                    bLimpiar.grid(row=len(boxes)+1, column=1, padx=10, pady=10)
                else:
                    confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                    if confirmacion:
                        try:
                            Coordinador.getUsuarioIngresado().agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                            messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")
                        except:
                            messagebox.showerror("Error", CampoInvalido().mostrarMensaje())
            except:
                messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

        titulo = Label(self, text="Agregar Materia", font=("Arial", 14), fg="#8B4513", bg="#D2B48C")
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        descripcion.pack(anchor="n", pady=20)

        sFrame = Frame(self, bg="#F5F5DC")  # Fondo claro de tonalidad café
        sFrame.pack()

        tituloC = Label(sFrame, text="Criterios", font=("Arial", 11), fg="white", bg="#8B4513")
        tituloC.grid(row=0, column=0, padx=10, pady=8)

        tituloV = Label(sFrame, text="Valores", font=("Arial", 11), fg="white", bg="#8B4513")
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        nombreL = Label(sFrame, text="Nombre", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        nombreL.grid(row=1, column=0, padx=10, pady=8)
        nombreE = Entry(sFrame, font=("Arial", 11))
        nombreE.grid(row=1, column=1, padx=10, pady=8)

        codigoL = Label(sFrame, text="Código", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        codigoL.grid(row=2, column=0, padx=10, pady=8)
        codigoE = Entry(sFrame, font=("Arial", 11))
        codigoE.grid(row=2, column=1, padx=10, pady=8)

        descripcionL = Label(sFrame, text="Descripción", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        descripcionL.grid(row=3, column=0, padx=10, pady=8)
        descripcionE = Entry(sFrame, font=("Arial", 11))
        descripcionE.grid(row=3, column=1, padx=10, pady=8)

        creditosL = Label(sFrame, text="Créditos", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        creditosL.grid(row=4, column=0, padx=10, pady=8)
        creditosE = Entry(sFrame, font=("Arial", 11))
        creditosE.grid(row=4, column=1, padx=10, pady=8)

        prerrequisitosL = Label(sFrame, text="# Prerrequisitos", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        prerrequisitosL.grid(row=5, column=0, padx=10, pady=8)
        prerrequisitosE = Entry(sFrame, font=("Arial", 11))
        prerrequisitosE.grid(row=5, column=1, padx=10, pady=8)

        facuL = Label(sFrame, text="Facultad", font=("Arial", 11), fg="#8B4513", bg="#D2B48C")
        facuL.grid(row=6, column=0, padx=10, pady=8)
        valores = Coordinador.getFacultades()
        facuE = ttk.Combobox(sFrame, values=valores, font=("Arial", 10))
        facuE.grid(row=6, column=1, padx=10, pady=8)

        botonSiguiente = Button(sFrame, text="Siguiente", command=siguiente, font=("Arial", 11), fg="white", bg="#8B4513")
        botonSiguiente.grid(row=7, column=0, padx=10, pady=10, sticky='e')

        botonLimpiar = Button(sFrame, text="Limpiar", command=limpiar1, font=("Arial", 11), fg="white", bg="#8B4513")
        botonLimpiar.grid(row=7, column=1, padx=10, pady=10)
