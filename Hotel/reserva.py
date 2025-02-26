from datetime import datetime  

class Reserva:
    lista_reservas = []

    def __init__(self, id, habitacion, fecha_entrada, fecha_salida, huesped):
        self.id = id
        self.habitacion = habitacion
        self.fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()  
        self.fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()    
        self.huesped = huesped
        Reserva.lista_reservas.append(self)

    def costo_total(self):
        dias = (self.fecha_salida - self.fecha_entrada).days  
        costototal = self.habitacion.costo * dias
        return f"El costo total de la habitación {self.habitacion.numero} será {costototal}."
