from ManejadorInscripciones import ManejadorInscripciones
from ManejadorPersonas import ManejadorPersonas
from ManejadorTalleres import ManejadorTalleres
from Persona import Persona
from Inscripcion import Inscripcion
import datetime
class Menu:
    __switcher=None
    __manejoinsc = ManejadorInscripciones()
    __manejoper = ManejadorPersonas()
    __manejotal = ManejadorTalleres()
    def __init__(self):
        self.__manejotal.manejarTalleres()
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        nombp = input("Ingrese nombre de la persona a inscribir: ")
        dirp = input("Ingrese la direccion de la persona a inscribir: ")
        dnip = input("Ingrese el DNI de la persona a inscribir: ")
        persona = Persona(nombp, dirp, dnip)
        self.__manejoper.agregarPersona(persona)
        idTal = input("Ingrese el ID del taller a inscribir: ")
        taller = self.__manejotal.buscarTaller(idTal)
        fecha = datetime.date.today()
        insc = Inscripcion(fecha, persona, taller)
        self.__manejotal.actualizarTaller(idTal, insc)
        self.__manejoinsc.agregarInscripcion(insc)
    def opcion2(self):
        dnip = input("Ingrese el DNI de la persona a buscar: ")
        buscar = self.__manejoinsc.buscarPersona(dnip)
        if (buscar != 0):
            print ("El nombre del taller a la que persona está inscripto es: ", buscar)
        else: print ("La persona no se encontró")
    def opcion3(self):
        idt = int(input("Ingrese el ID del taller a buscar: "))
        self.__manejoinsc.mostrarPersonasTaller(idt)

    def opcion4(self):
        dnip = input("Ingrese el DNI de la persona a actualizar: ")
        self.__manejoinsc.registrarPago(dnip)

    def opcion5(self):
        self.__manejoinsc.crearArchivo()
        print("El archivo se creó!")