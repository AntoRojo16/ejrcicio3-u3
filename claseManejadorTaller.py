import numpy as np
from claseTallerCapacitacion import TallerCapacitacion
from claseManejadorPersona import ManejadorPersona
from clasePersona import Persona
import csv
class ManejadorTaller:

    __cantida=0
    
    def agregar(self,unTaller):
        self.__tallerM[self.__cantida]=unTaller
        self.__cantida+=1

    def agregarOtro(self,unTaller):
        self.__tallerM[self.__cantida]=unTaller
        self.__cantida+=1
    def __init__(self):
        archivo=open("Talleres.csv")
        reader=csv.reader(archivo,delimiter=",")
        self.__cantida=0
        for fila in reader:
            if len(fila)==1:
                print(fila[0])
                dimension=int(fila[0])
                self.__tallerM=np.empty(dimension,dtype=TallerCapacitacion) 
            else:
                Id=fila[0]
                nombre=fila[1]
                vacantes=fila[2]
                monto=fila[3]
                unTaller=TallerCapacitacion(Id,nombre,vacantes,monto)
                self.agregarOtro(unTaller)
        archivo.close()


    def mostrarTalleres(self):
        for j in range(self.__cantida):
            print(self.__tallerM[j])

    def buscarNoombre (self, taller):
        i=0
        unTaller=self.__tallerM[i]
        nombreTaller=unTaller.getNom()
        while(i<=self.__cantida)and(str(nombreTaller)!=str(taller)):
            i+=1
            unTaller=self.__tallerM[i]
            nombreTaller=unTaller.getNom()
        
        if i<=self.__cantida:
            return i
        else:
            return False


    def insccribirPersona(self,personas,inscripciones):
        nombreTaller=input("Ingrese el  nombre de un taller: ")
        i=self.buscarNoombre(nombreTaller)
        print("el valor de i es {}".format(i))
        if type(i)==int:
            nombre=input("Ingrese el nombre de la persona: ")
            direccion=input("Ingrese la direccion: ")
            dni=input("ingrese el DNI: ")
            unaPersona=Persona(nombre, direccion, dni)
            personas.agregarPersona(unaPersona)
            self.__tallerM[i].iinscribirATaller(unaPersona,inscripciones)