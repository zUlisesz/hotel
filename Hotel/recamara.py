import json

class Recamara:
    recamaras = []

    def __init__(self, numero, tipo, camas, costonoche):
        self.numero = numero
        self.tipo = tipo
        self.camas = camas
        self.costo = costonoche
        self.disponibilidad = True
        Recamara.recamaras.append(self)

    @staticmethod
    def cargarRecamaras(file):
        try:
            with open(file, 'r') as file:
                data = json.load(file)
                for recamara_data in data:
                    Recamara(
                        recamara_data['numero'],
                        recamara_data['tipo'],
                        recamara_data['camas'],
                        recamara_data['costonoche'],
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
                'numero': recamara.numero,
                'tipo': recamara.tipo,
                'camas': recamara.camas,
                'costonoche': recamara.costonoche
                'disponibilidad': recamara.disponibilidad
            }
            existing_data.append(recamara_data)

        with open(file, 'w') as file:
            json.dump(existing_data, file, indent=4)

        Recamara.recamaras.clear()
