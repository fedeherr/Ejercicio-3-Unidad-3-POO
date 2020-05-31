from Taller import Taller
from Persona import Persona
import datetime
class Inscripcion:
    __fechaInscripcion = datetime.date.today()
    __pago = False
    __persona = None
    __taller = None
    def __init__(self, fechaInscripcion, persona, taller):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
    def getIdTal(self):
        return self.__taller.getNum()
    def getPersonaDni(self):
        return self.__persona.getDni()
    def getNombTaller(self):
        return self.__taller.getNomb()
    def getNumTaller(self):
        return self.__taller.getNum()
    def getPersona(self):
        return self.__persona.getPersona()
    def actPago(self):
        self.__pago = True
    def getFecha(self):
        return self.__fechaInscripcion
    def getPago(self):
        return self.__pago
    def __str__(self):
        return "%s %s %s" % (self.__pago, self.__persona.getDni(), self.__taller.getNum())