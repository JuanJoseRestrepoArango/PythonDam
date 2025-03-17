
class VideoJuego:
    horasEstimadasDefecto = 10
    entregadoDefecto = False

    def __init__(self, titulo = "", horasEstimadas = horasEstimadasDefecto, genero ="", compañia=""):
        self.__titulo = titulo
        self.__horasEstimadas = horasEstimadas
        self.__entregado = self.entregadoDefecto
        self.__genero = genero
        self.__compañia = compañia

    def setTitulo(self,titulo):
        self.__titulo = titulo
    
    def getTitulo(self):
        return self.__titulo
    
    def setHoras(self,numero):
        self.__horasEstimadas = numero
    
    def getHoras(self):
        return self.__horasEstimadas
    
    def setGenero(self,genero):
        self.__genero = genero
    
    def getGenero(self):
        return self.__genero
    
    def setCompañia(self,compañia):
        self.__compañia = compañia
    
    def getCompañia(self):
        return self.__compañia

    def entregar(self):
        self.__entregado = True

    def devolver(self):
        self.__entregado = False

    def isEntregado(self):
        return self.__entregado


    def compareTo(self,s):
        if(self.__horasEstimadas > s.__horasEstimadas):
            return self
        elif(self.__horasEstimadas < s.__horasEstimadas):
            return s
        else:
            return self
        
    def __str__(self) :
        return f'titulo = {self.__titulo} horasEstimadas = {self.__horasEstimadas} genero = {self.__genero} entregado = {self.__entregado} compañia = {self.__compañia} '

        