import numpy as np
from claseInscripcion import Inscripcion
class ManejadorInscripcion:
    __cantida=0
    __dimension=0
    __incremento=5


    def __init__(self,dimension,incremento=5):
        self.__inscripcion=np.empty(dimension,dtype=Inscripcion) 
        self.__cantida=0
        self.__dimension=dimension

    def agregar(self,unInscripcion):
        if self.__cantida==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripcion.resize(self.__dimension)
        self.__inscripcion[self.__cantida]=unInscripcion
        self.__cantida+=1
        

    def mostrarIscripcion(self):
        for i in range(self.__cantida):
            unaInscripcion=self.__inscripcion[i]
            unaInscripcion.mostrar()


    def ConsultarInscripcion(self):
        dni=input("ingresar el dni de la persona que se desea buscar")
        i=0
        unaIscripcion=self.__inscripcion[i]
        band=False
        while i<(self.__cantida)and band!=True:
            band=unaIscripcion.buscarPersona(dni)
            i+=1
            unaIscripcion=self.__inscripcion[i]
        if band==True:
            print("se encontro a la persona inscripta al ttaller")
            unaIscripcion=self.__inscripcion[i-1]
            unaIscripcion.mostrarDatos()

    
    def consultarInscriptos(self):
        ident=input("ingrese el identificador del taller ")
        for i in range(self.__cantida):
            self.__inscripcion[i].buscarTaller(ident)



    def registrarPago(self):
        dni=input("ingrese en dni de la persona ")
        i=0
        band=True
        unaInscripcion=self.__inscripcion[i]
        while(i<self.__cantida) and(band==True):
            band=unaInscripcion.cambiarPago(dni)
            i+=1
            unaInscripcion=self.__inscripcion[i]
        if band==False:
            print("se registro el pago")
        



        