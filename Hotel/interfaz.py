from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk 
from user import Usuario
from huesped import Huesped
from administrador import Administrador
from validacion import Validation

def loadfiles():
    Huesped.cargarHuepedes('huespedes.json')        
    Usuario.cargar_usuarios('users.json')
    

def ventanaAdmin():
    global windowAdmin
    window.withdraw()
    windowAdmin = Toplevel()
    windowAdmin.title('Ventana de administrador')
    windowAdmin.config(bg =  'AliceBlue')
    windowAdmin.resizable(width=False , height= False)
    
    admin = Image.open("C:/Users/PC/Desktop/hotel-main/hotel-main/Hotel/imgAdministrador-1.jpg").resize((560,424))
    adminTk = ImageTk.PhotoImage(admin)
    labelAdmin = Label(windowAdmin, image= adminTk)
    

    adminLabel = Label(windowAdmin, text = f'BIENVENIDO {(ulises.nombre).upper()}, HAS ACCEDIDO COMO ADMINISTRADOR', font = ('Agency Fb',30, 'bold'), padx = 30, pady = 6)

    botonCrear  = Button(windowAdmin , text = 'Crear Usuario'.upper() ,bg = 'CadetBlue3' ,font = ('Agency Fb',20, 'bold'), border = 4,padx = 26,  pady = 3, command = ventanaAdminAggHuesped)
    botonEliminar  = Button(windowAdmin, text = 'Eliminar Usuario'.upper(), bg = 'CadetBlue3',font = ('Agency Fb',20, 'bold'), border = 4, padx = 16 , pady = 3 )
    botonModificar  = Button(windowAdmin , text = 'Modificar usuario'.upper() ,bg = 'CadetBlue3', font = ('Agency Fb',20, 'bold'), border = 4,padx = 10 ,  pady = 3)
    botonCrearRecamara  = Button(windowAdmin , text = 'Crear recamara'.upper() ,bg = 'CadetBlue3', font = ('Agency Fb',20, 'bold'), border = 4,padx = 16 ,  pady = 3)
    botonVolver = Button(windowAdmin , text = 'Volver al inicio'.upper() ,bg = 'CadetBlue3', font = ('Agency Fb',20, 'bold'), border = 4,padx = 22,  pady = 3, command = lambda: volverInicio(windowAdmin))

    adminLabel.pack(pady = 18 )

    labelAdmin.pack(side= 'left', padx = 20)
    
    botonCrear.pack( padx = 20, pady = 11  )
    botonEliminar.pack(padx = 20 , pady = 11 )
    botonModificar.pack(padx = 20 , pady = 11)
    botonCrearRecamara.pack(padx = 20 , pady = 11 )
    botonVolver.pack(padx = 20 , pady = 10 )


    windowAdmin.mainloop()

def ventanaInicio():
    global window
    window = Tk()
    window.config(bg = 'AliceBlue')
    window.title('Log in')
    window.resizable(width= False, height= False)

    login = Image.open("C:/Users/PC/Desktop/hotel-main/hotel-main/Hotel/imagenHotel.jpg").resize((440,260))
    loginTk = ImageTk.PhotoImage(login)
    loginLabel  = Label(window , image= loginTk)

    global nombreEntry
    global passEntry
    
    nombreLabel = Label(window, text = 'USUARIO', font = ('Agency Fb',18, 'bold'))
    passLabel = Label(window, text = 'CONTRASEÑA', font = ('Agency Fb',18, 'bold'))

    nombreEntry = Entry(window, width= 24, font= ("Agency Fb",20), border = 4)
    passEntry = Entry(window, width  = 24 , show= '*', font = ("Agency Fb", 20), border = 4)

    botonEntrar = Button(window , text = 'ENTRAR', font = ('Agency Fb',20, 'bold'),bg = 'PaleGreen',border  = 4 , padx = 94, pady = 2, command= fboton )
    botonSalir  = Button(window , text = 'SALIR', font = ('Agency Fb',20, 'bold'),bg = 'PaleVioletRed',border  = 4,  padx = 104, pady = 2, command= window.quit)

    loginLabel.grid(row= 0 , column= 0 , columnspan= 2, padx = 10, pady =14 )

    nombreLabel.grid( row = 1 , column = 0  , pady = 18)
    passLabel.grid(row = 2 , column = 0 , pady = 18 )

    nombreEntry.grid( row = 1 , column= 1,pady  = 18 )
    passEntry.grid(row  = 2, column= 1, pady = 18)
    
    
    botonEntrar.grid(row = 3, column= 1, columnspan= 2 , pady = 14)
    botonSalir.grid(row = 4, column= 1, columnspan= 2, pady = 20)
    
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
    
    #windowRecepcionista.mainloop()    
    
def volverInicio(currentScreen):
    currentScreen.withdraw()
    window.deiconify()
    nombreEntry.delete( 0 , END)
    passEntry.delete(0 , END)

def fboton():
    nombre = nombreEntry.get()
    password = passEntry.get()
    
    if (Validation.usuarioExistente(Usuario.usuarios, nombre)):
        
        if (Validation.camposCompletos(nombre , password) ):   
                    
            user = Usuario.iniciar_sesion(nombre , password)
            if user.rol == 'administrador':
                ventanaAdmin()
            elif user.rol  == "recepcionista":
                ventanaRecepcionista()
            else:
                messagebox.showerror("Ups!", "Parece que no farmas parte del equipo de administradores\no no formas parte del equipo de recepcionistas")
        else:
            messagebox.showerror('Empty Fields','Completar todos los campos')
    else:
        nombreEntry.delete(0,END)
        messagebox.showerror('Not found','Usuario no existente')

ulises = Administrador('Ulises','administrador', 'marshal')
carlos = Usuario('Carlos','recepcionista','utf')

loadfiles()
ventanaInicio()
