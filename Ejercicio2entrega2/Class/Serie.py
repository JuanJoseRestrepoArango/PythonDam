
class Serie:
    numTempDefecto = 3
    entregadoDefecto = False

    def __init__(self,titulo = "", numTemp = numTempDefecto, genero = "", creador =""):
        self.__titulo = titulo
        self.__numTemp = numTemp
        self.__genero = genero
        self.__entregado = self.entregadoDefecto
        self.__creador = creador
    
    def setTitulo(self,titulo):
        self.__titulo = titulo
    
    def getTitulo(self):
        return self.__titulo
    
    def setNumero(self,numero):
        self.__numTemp = numero
    
    def getNumero(self):
        return self.__numTemp
    
    def setGenero(self,genero):
        self.__genero = genero
    
    def getGenero(self):
        return self.__genero
    
    def setCreador(self,creador):
        self.__creador = creador
    
    def getCreador(self):
        return self.__creador

    def entregar(self):
        self.__entregado = True

    def devolver(self):
        self.__entregado = False

    def isEntregado(self):
        return self.__entregado

    def compareTo(self,s):
        if(self.__numTemp > s.__numTemp):
            return self
        elif(self.__numTemp < s.__numTemp):
            return s
        else:
            return self
        
    def __str__(self) :
        return f'titulo = {self.__titulo} numeroTemporadas = {self.__numTemp} genero = {self.__genero} entregado = {self.__entregado} creador = {self.__creador} '
        