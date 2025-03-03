import json
class Huesped:
    huespedes = []

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        
    def descripcion(self):
        return "Nombre: {}, Télefono: {}".format(self.nombre, self.telefono)
        
    @staticmethod
    def guardarHuespedes(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        new_Huespedes = []
        for huesped in Huesped.huespedes:
            user_data = {
                'Nombre': huesped.nombre,
                'Tel': huesped.telefono
            }
            new_Huespedes.append(user_data)

        existing_data.extend(new_Huespedes)
        
    

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
            Huesped.huespedes.clear()
            print("Datos enviados correctamente a: {}".format(filename))
        except Exception as e:
            print("{}".format(e))
            
    
    @staticmethod
    def cargarHuepedes(filename):
        bool = False
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for i  , user_data in enumerate(data, start= 0):
                    required_fields = ['Nombre', 'Tel']
                    if all(field in user_data for field in required_fields):
                        Huesped(
                            nombre=user_data['Nombre'],
                            telefono =user_data['Tel']
                        )
                        bool = True
                    else:
                        print(f"first called failded, row {i} - {user_data}")
        except FileNotFoundError:
            print("Archivo {} no encontrado".format(filename))
            
        return bool
