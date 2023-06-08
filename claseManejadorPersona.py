import csv
from clasePersona import Persona
class ManejadorPersona:
    ___Personas=[]



    def __init__(self):
        self.___Personas=[]

    def agregarPersona(self,persona):
        self.___Personas.append(persona)

    def inicializar (self):
        archivo=open("Personas.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            nombre=fila[0]
            direccion=fila[1]
            dni=fila[2]
            unaPersona=Persona(nombre, direccion, dni)
            self.agregarPersona(unaPersona)


    def mostrar(self):
        for personas in self.___Personas:
            print(personas)

    
