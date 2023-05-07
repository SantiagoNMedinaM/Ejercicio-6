from claseviajerofrecuente import ViajeroFrecuente
import csv
class Controlador:
    __viajeros=[]
    def __init__(self):
        self.__viajeros = []
    def crearLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            nro=int(fila[0])
            dni=str(fila[1])
            nom=str(fila[2])
            ape=str(fila[3])
            tmil=int(fila[4])
            viajero=ViajeroFrecuente(nro,dni,nom,ape,tmil)
            self.__viajeros.append(viajero)
    """def buscar_viajero(self,n):
        i=0
        viajeroc=None
        while (i<len(self.__viajeros)):
            if self.__viajeros[i].getNum() == n:
                viajeroc=self.__viajeros[i]
            i+=1
        if viajeroc == None:
            print ("El numero de viajero ingresado es invalido")
        return viajeroc"""
    def mayorMillas(self):
        max_viajero = max(self.__viajeros)
        max_viajeros = [viajero for viajero in self.__viajeros if viajero == max_viajero]
        if len(max_viajeros) > 1:
            nombres = [viajero.getNombre() for viajero in max_viajeros]
            print("Los viajeros con mas millas acumuladas son: {}".format(nombres))
        else:
            print("El viajero con mas millas acumuladas es: {}".format(max_viajero.getNombre()))
    def sumar(self):
        print("Instancia c[2] antes de sumarle las millas:Nro:{}\tDNI:{}\tNombre:{}\tApellido:{}\tTotal Millas:{}".format(self.__viajeros[2].getNum(),self.__viajeros[2].getDni(),self.__viajeros[2].getNombre(),self.__viajeros[2].getApellido(),self.__viajeros[2].getTotal()))
        v=int(input("Ingrese Millas a sumar "))
        self.__viajeros[2]=self.__viajeros[2] + v
        print("Instancia c[2] despues de sumarle las millas:Nro:{}\tDNI:{}\tNombre:{}\tApellido:{}\tTotal Millas:{}".format(self.__viajeros[2].getNum(),self.__viajeros[2].getDni(),self.__viajeros[2].getNombre(),self.__viajeros[2].getApellido(),self.__viajeros[2].getTotal()))
    def restar(self):
        print("Instancia c[2] antes de sumarle las millas:Nro:{}\tDNI:{}\tNombre:{}\tApellido:{}\tTotal Millas:{}".format(self.__viajeros[2].getNum(),self.__viajeros[2].getDni(),self.__viajeros[2].getNombre(),self.__viajeros[2].getApellido(),self.__viajeros[2].getTotal()))
        m=int(input("Ingrese Millas a canjear "))
        self.__viajeros[2]=self.__viajeros[2] - m
        print("Instancia c[2] despues de canjear millas:Nro:{}\tDNI:{}\tNombre:{}\tApellido:{}\tTotal Millas:{}".format(self.__viajeros[2].getNum(),self.__viajeros[2].getDni(),self.__viajeros[2].getNombre(),self.__viajeros[2].getApellido(),self.__viajeros[2].getTotal()))


