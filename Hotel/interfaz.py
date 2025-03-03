from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk 
from user import Usuario
from huesped import Huesped
from administrador import Administrador

def loadfiles():
    
    if( Huesped.cargarHuepedes('huespedes.json') == True):
        print('data loaded successfuly')
    else:
        print('not having done that correctly, take this\n')
    

def ventanaAdmin():
    global windowAdmin
    window.withdraw()
    windowAdmin = Tk()
    windowAdmin.title('Ventana de administrador ')

    adminLabel = Label(windowAdmin, text = 'Bienvenido {}'.format(ulises.nombre), font = ('Agency Fb',24, 'bold'), padx = 40, pady = 6, bg= '#ADD8E6' )

    botonCrear  = Button(windowAdmin , text = 'Crear Usuario', font = ('Agency Fb',20, 'bold'), border = 4, pady = 3, command=ventanaAdminAggHuesped)
    botonEliminar  = Button(windowAdmin, text = 'Eliminar Usuario', font = ('Agency Fb',20, 'bold'), border = 4, pady = 3 )
    botonModificar  = Button(windowAdmin , text = 'Modificar usuario', font = ('Agency Fb',20, 'bold'), border = 4, pady = 3)
    botonCrearRecamara  = Button(windowAdmin , text = 'Crear recamara', font = ('Agency Fb',20, 'bold'), border = 4, pady = 3)

    adminLabel.grid(row = 0 , column= 0 ,columnspan= 2, pady = 18 )

    botonCrear.grid( row = 1, column= 0 , padx = 24, pady = 30 )
    botonEliminar.grid(row = 2, column= 0 , padx = 24 , pady = 30)
    botonModificar.grid(row  = 1, column= 1, padx = 24 , pady = 30)
    botonCrearRecamara.grid(row = 2 , column= 1, padx = 24 , columnspan= 30)


    windowAdmin.mainloop()

def ventanaInicio():
    global window
    window = Tk()
    window.config(bg = "white")
    window.title('Log in')

    login = Image.open("C:/Users/PC/Desktop/hotel-main/hotel-main/Hotel/icon.jpg")
    login = login.resize((200,200))
    loginTk = ImageTk.PhotoImage(login)
    loginLabel  = Label(window, image= loginTk)

    global nombreEntry
    global passEntry
    
    nombreLabel = Label(window, text = 'Usuario', font = ('Agency Fb',18, 'bold'), border= 2)
    passLabel = Label(window, text = 'Contraseña', font = ('Agency Fb',18, 'bold'),border = 2)

    nombreEntry = Entry(window, width= 24, font= ("Agency Fb",24))
    passEntry = Entry(window, width  = 24 , show= '*', font = ("Agency Fb", 24))

    boton = Button(window , text = 'Inicio', font = ('Agency Fb',20, 'bold'),border  = 4,  padx = 46, pady = 2, command= fboton)


    loginLabel.grid(row= 0 , column= 0 , columnspan= 2, padx = 60, pady =10 )

    nombreLabel.grid( row = 1 , column = 0 , padx = 20 , pady = 30)
    passLabel.grid(row = 2 , column = 0, padx = 20 , pady = 30 )

    nombreEntry.grid( row = 1 , column= 1 , padx = 20 ,pady  = 30 )
    passEntry.grid(row  = 2, column= 1, padx = 20 , pady = 30)

    boton.grid(row = 3, column= 0, columnspan= 2 , padx = 20 , pady = 14)

    window.mainloop()


def ventanaAdminAggHuesped(): 
    
    windowAdmin.withdraw()
    windowAdmin.deiconify()
    
    def onClose():
        Huesped.guardarHuespedes("huespedes.json")
        window.withdraw()

    def save():
        nombre = nombreEntry.get()
        tel = telEntry.get()
 
        ulises.registrar(Huesped(nombre  , tel))
        nombreEntry.delete(0,END)
        telEntry.delete(0,END)
        messagebox.showinfo("Registrado", "Huesped registrado de forma correcta")

    window = Tk()
    window.geometry("400x400")

    nombreLabel = Label(window, text ="Nombre del Huesped", font= ("Agency Fb",14, "bold"))
    nombreEntry = Entry(window )
    
    telLabel = Label(window, text ="Teléfono del huesped", font= ("Agency Fb",14, "bold"))
    telEntry = Entry(window )
    
    nombreLabel.pack(padx =20 , pady = 10)
    nombreEntry.pack(padx =20 , pady = 10)
    telLabel.pack(padx =20 , pady = 10)
    telEntry.pack(padx =20 , pady = 10)

    boton = Button(window , text = "Guardar Datos",font= ("Agency Fb",14, "bold"), command = save)
    volverAdminisrador = Button(window , text = 'Regresar',font= ("Agency Fb",14, "bold") , command= onClose)
    
    boton.pack(padx = 20 , pady =10 )
    volverAdminisrador.pack(padx= 20 , pady = 10)
    
    window.mainloop()
    
    
def ventanaRecepcionista():
    window.withdraw()
    global ventanaRecepcionista
    windowRecepcionista = Tk()
    window .title('Ventana e recepción')
    
    windowRecepcionista.mainloop()    
    

def fboton():
    nombre = nombreEntry.get()
    password = passEntry.get()
    user = Usuario.iniciar_sesion(nombre , password)
    if user.rol == 'administrador':
        ventanaAdmin()
    elif user.rol  == "recepcionista":
        ventanaRecepcionista()
    else:
        messagebox.showerror("Ups!", "Acceso denegado")


ulises = Administrador('Ulises','administrador', 'marshal')
carlos = Usuario('Carlos','recepcionista','utf')

loadfiles()
ventanaInicio()
