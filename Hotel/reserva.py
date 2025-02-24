class Rerserva:
    reservas = []
    def __init__(self,id , cuarto, fechaInicio, fechaFin):
        self.id = id
        self.ciuarto = cuarto
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        Rerserva.reservas.append(self)

    def costoTotal(self , id):
        total = id.costo * (self.fechaFin - self.fechaInicio)
        return "Costo total de la habitacion {}".format(total)
