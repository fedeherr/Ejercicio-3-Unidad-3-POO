from Taller import Taller
import csv
import numpy as np
class ManejadorTalleres:
    __arregloTalleres = None
    __cantidad = 0
    def __init__(self, arregloTalleres = None):
        self.__arregloTalleres = None
        self.__cantidad = 0
    def agregarTaller(self, unTaller):
        self.__arregloTalleres[self.__cantidad] = unTaller
        self.__cantidad += 1
    def buscarTaller(self, idTaller):
            for taller in self.__arregloTalleres:
                if (taller.getNum() == int(idTaller)):
                    return taller
            print ("No se encontró")
            return 0
    def actualizarTaller(self, idTaller, inscripcion):
            for taller in self.__arregloTalleres:
                if (taller.getNum() == idTaller):
                    taller.inscribirPersona(inscripcion)
    def manejarTalleres(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                self.__arregloTalleres = np.empty(int(fila[0]), dtype = Taller)
                bandera = not bandera
            else:
                    idTaller = int(fila[0])
                    nombre = fila[1]
                    vacantes = int(fila[2])
                    monto = float(fila[3])
                    unTaller = Taller(idTaller, nombre, vacantes, monto)
                    self.agregarTaller(unTaller)
    def getLongi(self):
        return self.__cantidad