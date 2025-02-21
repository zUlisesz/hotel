class Usuario:

    registros = []
    def __init__(self, nombre , rol, password):
        self.nombre = nombre 
        self.rol = rol
        self.__password = password

        Usuario.registros.append(self)

    def getPassword(sefl):
        return sefl.__password