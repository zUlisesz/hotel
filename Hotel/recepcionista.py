class Recpcionista(Usuario):

    def revisarisponibilidad(sefl, habitacion):
        if habitacion.disponibilidad:
            print(f"La habitación {habitacion.numero} está disponible.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible.")

    
    def reservar(sefl, habitacion, fecha_entrada, fecha_salida, huesped):
        if habitacion.disponibilidad:
            nueva_reserva = Reserva(len(Reserva.lista_reservas) + 1, habitacion, fecha_entrada, fecha_salida, huesped)
            habitacion.disponibilidad = False
            print(f"Reserva realizada exitosamente para la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible para reservar.")

    
    def canncelar(sefl , reserva):
        if reserva in Reserva.lista_reservas:
            reserva.habitacion.disponibilidad = True
            Reserva.lista_reservas.remove(reserva)
            print(f"Reserva {reserva.id} cancelada exitosamente.")
        else:
            print("Error: Reserva no encontrada.")
