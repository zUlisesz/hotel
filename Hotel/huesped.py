class Huesped:
    lista_huespedes = []

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        Huesped.lista_huespedes.append(self)
