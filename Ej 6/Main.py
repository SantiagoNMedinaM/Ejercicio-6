from claseviajerofrecuente import ViajeroFrecuente
from controlador import Controlador
from Menu import Menuclass
if __name__=="__main__":
    c=Controlador()
    c.crearLista()
    #n=int(input("Ingrese un numero de viajero "))
    #r=c.buscar_viajero(n) 
    #m=Menuclass()
    #if r!= None:
        #m.opciones(r)
    c.mayorMillas()
    c.sumar()
    c.restar()