from Inscripcion import Inscripcion
import numpy as np
import csv
class ManejadorInscripciones:
    __arr = None
    def __init__(self, i = 5):
        self.__arr = np.empty(i, dtype = Inscripcion)
        self.__total = i
        self.__contador = 0
    def agregarInscripcion(self, unaInscripcion):
        if (self.__contador != self.__total):
            self.__arr[self.__contador] = unaInscripcion
            print(self.__arr[self.__contador])
            self.__contador += 1
        else:
            self.__arr = np.append (arr, unaInscripcion)
            self.__total += 1
            self.__contador += 1 

    def buscarPersona(self, dni):
        for i in range(self.__contador):
            if (self.__arr[i].getPersonaDni() == dni):
                return (self.__arr[i].getNombTaller())
        return 0
    def mostrarPersonasTaller(self, num):
        for i in range(self.__contador):
            if (self.__arr[i].getNumTaller() == num):
                print (self.__arr[i].getPersona())
    def registrarPago(self, dni):
        for i in range(self.__contador):
            if (self.__arr[i].getPersonaDni() == dni):
                self.__arr[i].actPago()
                print ("Se actualizo el pago de la persona con DNI: ", dni)
                return()
        else: print ("Este DNI no esta inscripto")
    def crearArchivo(self):
        with open("inscripcion.csv", 'w') as archivo:
            for i in range(self.__contador):
                idp = self.__arr[i].getPersonaDni()
                idt = self.__arr[i].getIdTal()
                fec = self.__arr[i].getFecha()
                pago = self.__arr[i].getPago()
                datos = [idp, idt, fec, pago]   
                writer = csv.writer(archivo, delimiter=';')
                writer.writerow(datos) 

