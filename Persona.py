class Persona:
    __nombre = 'x'
    __direccion = 'x'
    __dni = 'x'
    def __init__(self, nombre = 'x', direccion = 'x', dni = 'x'):
        self.__direccion = direccion
        self.__nombre = nombre
        self.__dni = dni
    def getDni(self):
        return self.__dni
    def getPersona(self):
        return self
    def __str__(self):
        return "Nombre: %s \n Dirección %s \n DNI: %s" % (self.__nombre, self.__direccion, self.__dni)






        


