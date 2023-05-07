class ViajeroFrecuente:
    __nroviajero = 0
    __DNI = ""
    __nombre = ""
    __apellido = ""
    __totalmillas = 0
    def __init__(self,nroviajero=0,DNI="",nombre="",apellido="",totalmillas=""):
         self.__nroviajero = nroviajero
         self.__DNI = DNI
         self.__nombre = nombre
         self.__apellido = apellido
         self.__totalmillas = totalmillas
    def cantidadTotalDeMillas(self):
         #print("Total de millas: {}" .format(self.__totalmillas))
         return self.__totalmillas
    #def acumularMillas(self):
         cmillas=int(input("Ingrese millas a acumular "))
         self.__totalmillas+=cmillas
         return self.__totalmillas
    #def canjearMillas(self):
         canjear=int(input("Ingrese cantidad de millas a canjear "))
         if canjear >= self.__totalmillas:
              self.__totalmillas-=canjear
         else:
              print("No tiene suficientes millas para realizar el canje ")
         return self.__totalmillas
    def getDni(self):
        return self.__DNI
    def getApellido(self):
        return self.__apellido
    def getNum(self):
     return self.__nroviajero
    def getNombre(self):
        return self.__nombre
    def getTotal(self):
        return self.__totalmillas
    def __gt__(self, OtroViajero):
        return self.cantidadTotalDeMillas() > OtroViajero.cantidadTotalDeMillas()
    def __add__ (self, v):
        self.__totalmillas = self.__totalmillas + v
        return ViajeroFrecuente(self.__nroviajero, self.__DNI, self.__nombre, self.__apellido, self.__totalmillas)
    def __sub__ (self, m):
        self.__totalmillas = self.__totalmillas - m
        return ViajeroFrecuente(self.__nroviajero, self.__DNI, self.__nombre, self.__apellido, self.__totalmillas)
