from clasePersona import Persona
from claseTallerCapacitacion import TallerCapacitacion
from claseManejadorPersona import ManejadorPersona
from claseManejadorTaller import ManejadorTaller
from claseManejadorInscripcion import ManejadorInscripcion
if __name__=="__main__":
    ListaPersonas=ManejadorPersona()
    inscripciones=ManejadorInscripcion(3)
    #ListaPersonas.inicializar()
    talleres=ManejadorTaller()
    #talleres.inicializar()
    talleres.mostrarTalleres()
    talleres.insccribirPersona(ListaPersonas, inscripciones)
    talleres.insccribirPersona(ListaPersonas, inscripciones)
    #talleres.insccribirPersona(ListaPersonas, inscripciones)
    #talleres.insccribirPersona(ListaPersonas, inscripciones)
    #talleres.insccribirPersona(ListaPersonas, inscripciones)
    print("Las personas inscriptas son:")
    ListaPersonas.mostrar()
    print("las inscripciones realizadas son")
    inscripciones.mostrarIscripcion()
    #inscripciones.ConsultarInscripcion()
    #inscripciones.consultarInscriptos()
    inscripciones.registrarPago()
    