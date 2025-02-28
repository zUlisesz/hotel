from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk 

class Usuario:
    lista_usuario = []

    def __init__(self, Nombre, Rol, Password):
        self.nombre = Nombre
        self.rol = Rol
        self.__pass = Password
        Usuario.lista_usuario.append(self)


    def info(self):
        return f"El usuario se llama {self.nombre}, tiene rol de {self.rol}"
    

    @classmethod
    def iniciar_sesion(cls, nombre, password):
        for usuario in Usuario.lista_usuario:
            if usuario.nombre == nombre and usuario._Usuario__pass == password:
                print(f"Bienvenido {usuario.nombre}, acabas de iniciar sesión")
                return usuario
        print("Datos incorrectos para inicio de sesión")
        return None
    

def ventanaAdmin():
    window2 = Tk()
    window2.title('Ventana de administrador ')

    adminLabel = Label(window2, text = 'Bienvenido administrador', font = ('Agency Fb',18, 'bold'), padx = 40, pady = 6, bg= '#ADD8E6' )

    botonCrear  = Button(window2 , text = 'Crear Usuario', font = ('Agency Fb',18, 'bold'), border = 4)
    botonEliminar  = Button(window2 , text = 'Eliminar Usuario', font = ('Agency Fb',18, 'bold'), border = 4)
    botonModificar  = Button(window2 , text = 'Modificar usuario', font = ('Agency Fb',18, 'bold'), border = 4)
    botonCrearRecamara  = Button(window2 , text = 'Crear recamara', font = ('Agency Fb',18, 'bold'), border = 4)

    adminLabel.grid(row = 0 , column= 0 ,columnspan= 2)

    botonCrear.grid( row = 1, column= 0 , padx = 10 , pady = 16)
    botonEliminar.grid(row = 2, column= 0 , padx = 10 , pady = 16)
    botonModificar.grid(row  = 1, column= 1, padx = 10 , pady = 16)
    botonCrearRecamara.grid(row = 2 , column= 1, padx = 10 , columnspan= 16)


    window2.mainloop()

def ventanaInicio():
    window = Tk()
    window.title('Log in')

    login = Image.open('C:/Users/DELL/Downloads/icono.png').resize((200,200))
    loginTk = ImageTk.PhotoImage(login)
    loginLabel = Label(window, image= loginTk)


    nombreLabel = Label(window, text = 'Usuario', font = ('Agency Fb',18, 'bold'), border= 2)
    passLabel = Label(window, text = 'Contraseña', font = ('Agency Fb',18, 'bold'),border = 2)

    nombreEntry = Entry(window, width= 24, highlightthickness= 5)
    passEntry = Entry(window, width  = 24 , show= '*')

    boton = Button(window , text = 'Inicio', font = ('Agency Fb',20, 'bold'),border  = 4,  padx = 46, pady = 2, command= fboton)


    loginLabel.grid(row= 0 , column= 0 , columnspan= 2, padx = 60, pady =10 )

    nombreLabel.grid( row = 1 , column = 0 , padx = 20 , pady = 30)
    passLabel.grid(row = 2 , column = 0, padx = 20 , pady = 30 )

    nombreEntry.grid( row = 1 , column= 1 , padx = 20 ,pady  = 30 )
    passEntry.grid(row  = 2, column= 1, padx = 20 , pady = 30)

    boton.grid(row = 3, column= 0, columnspan= 2 , padx = 20 , pady = 14)

    window.mainloop()

    
    def fboton():
        nombre = nombreEntry.get()
        password = passEntry.get()
        piloto = Usuario.iniciar_sesion(nombre , password)
        if piloto.rol == 'administrador':
            ventanaAdmin()
        else:
            messagebox.showerror("Ups!", "Acceso denegado")
