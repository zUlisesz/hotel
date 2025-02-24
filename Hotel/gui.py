from tkinter import *
from user import Usuario
from tkinter import messagebox

def onClose():
    Usuario.guardar_usuarios("users.json")
    window.destroy()

def save():
    nombre = nombreEntry.get()
    rol  = rolEntry.get()
    password = passEntry.get()

    Usuario(nombre ,rol , password)
    messagebox.showinfo("Registrado", "Usuario guardado exitosamente")

window = Tk()
window.geometry("400x400")

nombreLabel = Label(window, text ="Ingresa tu nombre ", font= ("Agency Fb",14, "bold")).pack(padx =20 , pady = 10)
nombreEntry = Entry(window )
nombreEntry.pack(padx =20 , pady = 10)

rolLabel = Label(window, text ="Ingresa tu rol ", font= ("Agency Fb",14, "bold")).pack(padx =20 , pady = 10)
rolEntry = Entry(window )
rolEntry.pack(padx =20 , pady = 10)


passLabel = Label(window, text ="Ingresa tu contraseñaa", font= ("Agency Fb",14, "bold")).pack(padx =20 , pady = 10)
passEntry = Entry(window , show= "*")
passEntry.pack(padx =20 , pady = 10)


boton = Button(window , text = "Guardar Datos",font= ("Agency Fb",14, "bold"), command = save).pack(padx = 20 , pady =10 )


window.protocol("WM_DELETE_WINDOW", onClose)
window.mainloop()
