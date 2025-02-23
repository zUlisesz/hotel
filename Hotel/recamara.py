import json

class Recamara:
    recamaras = []

    def __init__(self, nombre, size, precio):
        self.nombre = nombre
        self.size = size
        self.precio = precio
        self.disponibilidad = True
        Recamara.recamaras.append(self)

    @staticmethod
    def cargarRecamaras(file):
        try:
            with open(file, 'r') as file:
                data = json.load(file)
                for recamara_data in data:
                    Recamara(
                        recamara_data['nombre'],
                        recamara_data['size'],
                        recamara_data['precio'],
                        recamara_data[True]
                    )
        except FileNotFoundError:
            pass

    @staticmethod
    def guardarRecamaras(file):
        try:
            with open(file, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        for recamara in Recamara.recamaras:
            recamara_data = {
                'nombre': recamara.nombre,
                'size': recamara.size,
                'precio': recamara.precio,
                'disponibilidad': recamara.disponibilidad
            }
            existing_data.append(recamara_data)

        with open(file, 'w') as file:
            json.dump(existing_data, file, indent=4)

        Recamara.recamaras.clear()
