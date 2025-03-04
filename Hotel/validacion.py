#clase auxiliar para hara realizar validaciones
class Validation:
    
    #método estático para verificar que el el nombre de un usuario sea existente dentro del sistema
    @staticmethod
    def usuarioExistente( usuarios, nombre):
        pasar = False
        for us in usuarios:
            if(us.nombre == nombre):
                pasar = True
    
        return pasar
    
    #metodo estáticopara verificar que dos campos no estén vacios
    @staticmethod
    def camposCompletos(nombre, password):
        if(password != "" and nombre != ""):
            pasar = True
        else:
            pasar = False
        
        return pasar
