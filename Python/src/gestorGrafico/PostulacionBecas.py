from tkinter import *
from tkinter import ttk  # Usamos ttk para asegurar mejor compatibilidad con macOS
from gestorGrafico.CrearBeca import CrearBeca
from gestorGrafico.EliminarBeca import EliminarBeca
from gestorGrafico.AplicarBeca import AplicarBeca
from gestorGrafico.MostrarBeca import MostrarBeca
from gestorGrafico.FieldFrame import FieldFrame

class PostulacionBecas(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#8B4513", highlightthickness=3, bg="#F5F5DC")
        self.pack(expand=True)
        
        # Funciones para cambiar entre ventanas
        def mostrarBeca():
            self.pack_forget()
            mBeca = MostrarBeca(ventana)
            mBeca.pack()

        def aplicarBeca():
            self.pack_forget()
            aBeca = AplicarBeca(ventana)
            aBeca.pack()

        def becaNueva():
            self.pack_forget()
            cBeca = CrearBeca(ventana)
            cBeca.pack()

        def eliminarBeca():
            self.pack_forget()
            eBeca = EliminarBeca(ventana)
            eBeca.pack()

        # Etiqueta de título
        tituloenventana = Label(self, text="Búsqueda y Postulación de Becas", bg="#F5F5DC", foreground="#8B4513", font=("Helvetica", 14, "bold"))
        tituloenventana.pack(side="top", anchor="c", padx=5, pady=5)
        
        # Descripción
        textodescriptivo = ("Esta funcionalidad permite:\n1.Ver listado de becas. \n2.Aplicar beca a estudiante." +
                           "\n3.Crear nueva beca. \n4.Eliminar beca.")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 16), bg="#D7B299", fg="#110433")
        descripcion.pack(anchor="n", pady=20, padx=5)

        # Marco para los botones
        seleccion = Frame(self, bg="#F5F5DC")
        seleccion.pack(padx=5, pady=5)

        # Botones usando ttk para asegurar compatibilidad y mejor apariencia en macOS
        mostrarB = ttk.Button(seleccion, text="Mostrar listado de becas", command=mostrarBeca)
        mostrarB.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        aplicarB = ttk.Button(seleccion, text="Aplicar beca a estudiante", command=aplicarBeca)
        aplicarB.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        crearB = ttk.Button(seleccion, text="Crear nueva beca", command=becaNueva)
        crearB.grid(row=1, column=0, padx=45, pady=10, sticky="w")

        eliminarB = ttk.Button(seleccion, text="Eliminar beca", command=eliminarBeca)
        eliminarB.grid(row=1, column=1, padx=50, pady=10, sticky="w")

        # Forzar la actualización de la interfaz para evitar problemas de renderizado en macOS
        self.update_idletasks()

# Ejecución de la aplicación
if __name__ == "__main__":
    root = Tk()
    root.title("Sistema Matricula de Materias")
    root.geometry("600x400")
    root.config(bg="#F5F5DC")  # Configura el fondo de la ventana principal

    app = PostulacionBecas(root)
    app.pack(expand=True, fill="both")

    root.mainloop()
