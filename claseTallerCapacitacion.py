from claseInscripcion import Inscripcion
from claseManejadorInscripcion import ManejadorInscripcion
class TallerCapacitacion:
    __id=0
    __nombre=""
    __vacantes=0
    __monto=0
    __inscripciones=None


    def __init__ (self,id,nombre,vacantes,monto):
        self.__id=id
        self.__nombre=nombre
        self.__vacantes=int(vacantes)
        self.__monto=monto
        self.__inscripciones=[]


    def verificarVacantes(self,unaInscripcion):
        bandera=False
        if int(self.__vacantes)>0:
            print("Hay vacantes disponibles")
            self.__inscripciones.append(unaInscripcion)
            bandera=True
            
        else:
            print("No hay vacantes disponibles")
        return bandera

    def realizarInscripcion(self,unaInscripcion):
        #unaInscripcion=Inscripcion(fecha, pago, self, persona)
        band=self.verificarVacantes(unaInscripcion)
        if band==True:
            print("La inscripcion se realizo correctamente")
            self.__vacantes-=1
        else:
            print("No se pudo relizar la inscripcion")
        


    def mostrar (self):
        for inscripcion in self.__inscripciones:
            print(inscripcion)
    


    def __str__(self) :
        return("Id de taller: {}, Nombre: {}, Vacante: {}, Monto: {}".format(self.__id,self.__nombre,self.__vacantes,self.__monto))


    def getNom(self):
        return self.__nombre


    def iinscribirATaller(self,unaPersona,inscripciones):
        fecha=input("Ingrese la fecha en la que se va arealizar la inscripcion")
        unaInscripcion=Inscripcion(fecha, self, unaPersona)
        inscripciones.agregar(unaInscripcion)
        self.realizarInscripcion(unaInscripcion)


    def getMonto(self):
        return self.__monto

    def getId(self):
        return self.__id




