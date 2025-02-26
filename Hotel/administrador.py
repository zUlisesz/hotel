class Administrador(Usuario):

    def registrar(self,huesped):
        if isinstance(huesped, Huesped):
            Huesped.lista_huespedes.append(huesped)
            print(f"Huesped {huesped.nombre} registrado exitosamente.")
        else:
            print("Error: El objeto no es un Huesped válido.")

    def modificarCliente(self , huesped):
        if huesped in Huesped.lista_huespedes:
            if nuevo_nombre:
                huesped.nombre = nuevo_nombre
            if nuevo_telefono:
                huesped.telefono = nuevo_telefono
            print(f"Huesped {huesped.nombre} modificado exitosamente.")
        else:
            print("Error: Huesped no encontrado.")

    def eliminarUsuario(self, huesped):
        if huesped in Huesped.lista_huespedes:
            Huesped.lista_huespedes.remove(huesped)
            print(f"Huesped {huesped.nombre} eliminado exitosamente.")
        else:
            print("Error: Huesped no encontrado.")

    def crearRecamara(self, numero, tipo, camas, costonoche):
        nueva_habitacion = Habitacion(numero, tipo, camas, costonoche)
        print(f"Habitación {nueva_habitacion.numero} creada exitosamente.")
