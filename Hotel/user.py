import json

class Usuario:
    usuarios = []

    def __init__(self, nombre, rol, password):
        self.nombre = nombre
        self.rol = rol
        self.password = password
        Usuario.usuarios.append(self)
        
    def getInfo(self):
        return "Nombre :{}, Rol: {}\n".format(self.nombre, self.rol)

    @staticmethod
    def cargarUsuarios(file):
        try:
            with open(file, 'r') as file:
                data = json.load(file)
                for user_data in data:
                    Usuario(user_data['nombre'], user_data['rol'], user_data['password'])
        except FileNotFoundError:
            pass

    @staticmethod
    def guardarUsuarios(file):
        try:
            with open(file, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        for user in Usuario.usuarios:
            user_data = {
                'nombre': user.nombre,
                'rol': user.rol,
                'password': user.password
            }
            existing_data.append(user_data)

        with open(file, 'w') as file:
            json.dump(existing_data, file, indent=4)

        Usuario.usuarios.clear()
