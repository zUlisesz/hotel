import json
from tkinter import messagebox
class Usuario:
    usuarios = []

    def __init__(self, nombre, rol, password):

        self.nombre = nombre
        self.rol = rol
        self.__password = password
        Usuario.usuarios.append(self)

    def get_info(self):
        return f"Nombre: {self.nombre}, Rol: {self.rol}\n"

    @staticmethod
    def cargar_usuarios(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for user_data in data:
                    required_fields = ['nombre', 'rol', 'password']
                    if all(field in user_data for field in required_fields):
                        Usuario(
                            nombre=user_data['nombre'],
                            rol=user_data['rol'],
                            password=user_data['password']
                        )
                    else:
                        print(f"Skipping invalid user data: {user_data}")
        except FileNotFoundError:
            print("Archivo {} no encontrado".format(filename))
            

    @staticmethod
    def guardar_usuarios(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        new_users = []
        for user in Usuario.usuarios:
            user_data = {
                'nombre': user.nombre,
                'rol': user.rol,
                'contraseña': user.__password
            }
            new_users.append(user_data)

        existing_data.extend(new_users)

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
            Usuario.usuarios.clear()
            print("Datos enviados correctamente a: {}".format(filename))
        except Exception as e:
            print("{}".format(e))
            
        
    @classmethod
    def iniciar_sesion(cls, nombre, password):
        verdadero = False
        for usuario in Usuario.usuarios:
            if usuario.nombre == nombre and usuario._Usuario__password == password:
                print(f"Bienvenido {usuario.nombre}, acabas de iniciar sesión")
                verdadero = True
                return usuario

        if verdadero == False:
            messagebox.showinfo('Erro','usuario no existente')
            
        return None
