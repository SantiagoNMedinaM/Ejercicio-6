from claseviajerofrecuente import ViajeroFrecuente
from controlador import Controlador
class Menuclass:
    __opcion=0
    def __init__(self):
        self.__opcion=0
    def opciones(self, r):
        while True:
            print ("Opcion 1: Consultar millas")
            print ("Opcion 2: Acumular millas")
            print ("Opcion 3: Canjear millas")
            print ("Opcion 4: Salir")
            self.__opcion=int(input("Seleccione una opcion "))
            if self.__opcion==1:
                r.cantidadTotalDeMillas()
            elif self.__opcion==2:
                r.acumularMillas()
            elif self.__opcion==3:
                r.canjearMillas()
            elif self.__opcion==4:
                break
            else:
                print("La opcion ingresada no es valida, ingrese otra opcion")
                


                   
                   