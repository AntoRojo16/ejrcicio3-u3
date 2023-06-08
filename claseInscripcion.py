class Inscripcion:
    __fecha=""
    __pago=bool
    __taller=None
    __persona=None


    def __init__(self,fecha,unTaller,unaPersona,pago=False):
        self.__fecha=fecha
        self.__pago=pago
        self.__taller=unTaller
        self.__persona=unaPersona

    def __str__(self):
        cadena=("Fecha de inscripcion: {} Estado de pago: {} \n".format(self.__fecha,self.__pago))
        cadena+=str(self.__persona)+"\n"
        return  cadena

    def mostrar (self):
        print("Fecha de inscripcion: {} Estado de pago: {} \n".format(self.__fecha,self.__pago))
        print(self.__persona)
        print(self.__taller)


    def buscarPersona(self,dni):
        band=False
        if int(self.__persona.getDni())==int(dni):
            band=True
        return band

    def mostrarDatos(self):
        print(" El taller al que esta inscripto es  {}".format(self.__taller.getNom()))
        print("la cantidad de adeuda es {}".format(self.__taller.getMonto()))


    def buscarTaller(self,ident):
        if self.__taller.getId()==ident:
            print(self.__persona)
        else:
            print("este no es el  taller")


    def getDniPer(self):
        return self.__persona.getDni()


    def cambiarPago(self,dni):
        band=True
        if int(dni)==int(self.__persona.getDni()):
            self.__pago=True
            band=False
            return band

        else:
            return band

            

      
