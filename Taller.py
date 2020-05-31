class Taller:
    __idTaller = 0
    __nombre = 'x'
    __vacantes = 0
    __montoinscripcion = 0
    __inscripciones = None
    def __init__(self, idTaller = 0, nombre = 'x', vacantes = 0, montoinscripcion = 0):
        self.__montoinscripcion = montoinscripcion
        self.__idTaller = idTaller
        self.__vacantes = vacantes
        self.__nombre = nombre
        self.__inscripciones = []
    def inscribirPersona(self, inscripcion):
        if (self.__vacantes > 0):
            self.__inscripciones.append(inscripcion)
            self.__vacantes = self.__vacantes - 1
        else: print("No hay vacantes")
    def getNum(self):
        return self.__idTaller
    def getNomb(self):
        return self.__nombre
