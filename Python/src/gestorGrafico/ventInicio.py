#Juan Miguel Ochoa/Sebastian Martinez/David Posada/Juan Diego Sanchez/Daniel Zambrano

from tkinter import *

class VentInicio(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.pack()

        # Creación de Frames
        p1Frame = Frame(self, height=450, width=425, bg="#F5E6C4")
        p1Frame.grid(row=0, column=0, sticky="nsew", padx=(5, 0), pady=5)
        p1Frame.grid_propagate(False)

        p2Frame = Frame(self, height=450, width=425, bg="#F5E6C4")
        p2Frame.grid(row=0, column=1, sticky="nsew", padx=(0, 5), pady=5)
        p2Frame.grid_propagate(False)

        p3Frame = Frame(p1Frame, height=70, width=415, bg="#D7B299")
        p3Frame.grid(row=0, column=0, columnspan=1, rowspan=1, padx=5, pady=(5, 3))
        p3Frame.pack_propagate(False)

        p4Frame = Frame(p1Frame, height=365, width=415, bg="#F5E6C4")
        p4Frame.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=(3, 5))
        p4Frame.pack_propagate(False)

        p5Frame = Frame(p2Frame, height=100, width=415, bg="#F5D5B0")
        p5Frame.grid(row=0, column=0, columnspan=1, rowspan=1, padx=5, pady=(5, 3))
        p5Frame.pack_propagate(False)

        p6Frame = Frame(p2Frame, height=335, width=335, bg="#8B5A2B")
        p6Frame.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=(3, 5))
        p6Frame.grid_propagate(False)

        # Frame 3 Saludo bienvenida
        mensaje = "Hola, bienvenido al sistema de administracion academica UniAdmin."
        mensajeBienv = Label(p3Frame, text=mensaje, font=("Arial", 18, "bold"), bg="#F5D5B0", wraplength=415, fg="#6D4C41")
        mensajeBienv.pack(expand=True)

        # Frame 5 Bibliografía de cada desarrollador
        bibi1 = "Hola, Soy Juan Miguel Ochoa Agudelo, nacido en Medellín un 23 de octubre de 2005. Estoy cursando segundo semestre en ingeniería de sistemas en la Universidad Nacional de Colombia. Soy un gran aficionado al futbol y a la informática desde hace mucho tiempo."
        bibi2 = "Soy Sebastián Martínez Sequeira, nací el 10 de Mayo de 2006 en Cesar, Valledupar, estoy en mi segundo semestre de Ing. de Sistemas. Me considero un chico apasionado por el deporte, curioso, ademas me gusta ser un apoyo importante para la gente que me rodea."
        bibi3 = "Hola, soy David, actualmente estoy estudiando ingeniería de sistemas en la UNAL, donde también represento al equipo competitivo en fútbol sala. Regularmente me gusta viajar con mi familia y reunirme con mi grupo de amigos para compartir lo que hacemos en la semana."
        bibi4 = "Mi nombre es Juan Diego Sánchez , nacido en santa Marta el 10 de Julio de 2002, actualmente curso tercer semestre de ingeniería en sistemas e informática. Apasionado por el futbol, queriendo entrar al mundo de la informática y deseando conocer el mundo entero."
        bibi5 = "Soy Daniel Zambrano nacido en Duitama, boyacá tengo 25 años y estoy cursando el 5to semestre de ingeniería de sistemas, me interesa la natación, el senderismo y disfrutar en familia."

        self.biblios = [bibi1, bibi2, bibi3, bibi4, bibi5]
        self.punteroIntergrante = 1

        def cambiarTextoEImagenF6(evento):
            i = self.punteroIntergrante
            
            # Cambio de texto
            evento.widget["text"] = self.biblios[i]
            
            # Cambio de imágenes
            imag1 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgIn{0}_1.png".format(i+1))     
            imag2 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgIn{0}_2.png".format(i+1))     
            imag3 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgIn{0}_3.png".format(i+1))     
            imag4 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgIn{0}_4.png".format(i+1))     
            
            global lisImagenes  # Es global para no perder el puntero de las imágenes cuando el método finalice
            lisImagenes = [imag1, imag2, imag3, imag4]
            
            setCuatroImagenes(lisImagenes)
            
            # Cambio de puntero  
            i += 1
            n = 5  # número de grupo de fotos en la carpeta imágenes, cuando se tengan todas debe ser 5
            if i == n:
                self.punteroIntergrante = 0
            else:
                self.punteroIntergrante = i
        
        biblioTexto = Label(p5Frame, text=bibi1, font=("Arial", 10), bg="#F5E6C4", wraplength=405, highlightbackground="#8B5A2B", highlightthickness=2)
        biblioTexto.pack(expand=True, fill="both")
        biblioTexto.bind("<Button-1>", cambiarTextoEImagenF6) # Evento de click izquierdo

        # Frame 6 Imágenes
        def setCuatroImagenes(packImagenes):
            img1.config(image=packImagenes[0])
            img2.config(image=packImagenes[1])
            img3.config(image=packImagenes[2])
            img4.config(image=packImagenes[3])

        tam = 157
        
        self.image1 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgln1_1.png")
        self.image2 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgln1_2.png")
        self.image3 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgln1_3.png")
        self.image4 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgln1_4.png")

        img1 = Label(p6Frame, image=self.image1, height=tam, width=tam)
        img1.grid(row=0, column=0, columnspan=1, rowspan=1, padx=3, pady=3)

        img2 = Label(p6Frame, image=self.image2, height=tam, width=tam)
        img2.grid(row=0, column=1, columnspan=1, rowspan=1, padx=3, pady=3)

        img3 = Label(p6Frame, image=self.image3, height=tam, width=tam)
        img3.grid(row=1, column=0, columnspan=1, rowspan=1, padx=3, pady=3)

        img4 = Label(p6Frame, image=self.image4, height=tam, width=tam)
        img4.grid(row=1, column=1, columnspan=1, rowspan=1, padx=3, pady=3)
        
        # Frame 4
        # Imagen
        self.punteroImagen = 2
        
        def cambiarTextoEImagenF4(evento):
            i = self.punteroImagen

            # Cambio de imágenes
            global imagF4
            imagF4 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgInF4.{0}.png".format(i))     
   
            ImagenF4.config(image=imagF4)
            
            # Cambio de puntero  
            i += 1
            n = 5  # número de grupo de fotos en la carpeta imágenes, cuando se tengan todas debe ser 5
            if i == (n + 1):
                self.punteroImagen = 1
            else:
                self.punteroImagen = i
        
        self.imagenF41 = PhotoImage(file="Python/src/gestorGrafico/Imagenes/imgInF4.1.png")
        #ajuste al marco que no servia para nada
        ImagenF4 = Label(p4Frame, image=self.imagenF41, width=300,
                 wraplength=160, borderwidth=4, relief="solid",)

        ImagenF4.pack(side="top",pady=3)
        ImagenF4.bind("<Enter>",cambiarTextoEImagenF4)  # Evento de pasar el mouse por encima
        
        # Texto descripcion
        
        descripTexto = Label(p4Frame,text="",font=("arial", 14, "bold"),bg="#F5E6C4",wraplength=400)
        descripTexto.pack(side="top",fill="x",pady=10)
        
        # Boton para pasar
        
        def cambioVentana():
            self.destroy()           
            ventana.abrirLog()
            
        
        botonIngreso=Button(p4Frame,text="Ingresar",command=cambioVentana,bg="#8B5A2B",font=("arial", 12, "bold"),fg="#F5E6C4")
        botonIngreso.pack(side="top",pady=(10,20))
           
        
        # Creacion del menu :U
        ventana.menuBar = Menu(ventana)
        ventana.option_add("*tearOff",  False)
        ventana.config(menu=ventana.menuBar)
        menu1= Menu(ventana.menuBar)
        ventana.menuBar.add_cascade(label="Archivo",menu=menu1)
        menu1.add_command(label="Salir",command=lambda:ventana.destroy())
        
        textDescrip="UniAdmin es un sistema de gestión académica diseñado para mejorar la administración de asignaturas en instituciones educativas. Está dirigido exclusivamente a coordinadores académicos y tiene como objetivo optimizar los procesos relacionados con la gestión académica."
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))