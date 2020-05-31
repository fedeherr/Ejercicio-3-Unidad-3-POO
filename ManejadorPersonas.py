from Persona import Persona
class ManejadorPersonas:
    __listaPersonas = []
    def __init__(self, listaPersonas = []):
        self.__listaPersonas = listaPersonas
    def agregarPersona(self, unaPersona):
        self.__listaPersonas.append(unaPersona)
