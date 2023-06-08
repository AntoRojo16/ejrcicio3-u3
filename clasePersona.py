class Persona:
    __nonmbre=""
    __direccon=""
    __dni=0



    def __init__ (self,nombre,direccion,dni):
        self.__nonmbre=nombre
        self.__direccon=direccion
        self.__dni=dni


    def __str__ (self):
        return ("Nombre: {}, Direcion: {}, DNI: {}".format(self.__nonmbre,self.__direccon,self.__dni))


    def getDni(self):
        return self.__dni


    def getNNombre(self):
        return self.__nonmbre
