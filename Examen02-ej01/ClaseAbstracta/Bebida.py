class Bebida:
    def __init__(self,identificador = 0,cantidadLitros = 0,precio = 0, marca ="") :
        self.identificador = identificador
        self.cantidadLitros = cantidadLitros
        self.precio = precio
        self.marca = marca

    def getIdentificador(self):
        return self.identificador
    def getCantidadLitros(self):
        return self.cantidadLitros
    def getPrecio(self):
        return self.precio
    def getMarca(self):
        return self.marca
    
    def setIdentificador(self, identificador):
        self.identificador =identificador
    def setCantidadLitros(self, cantidadLitros):
        self.cantidadLitros = cantidadLitros
    def setPrecio(self, precio):
        self.precio = precio
    def setMarca(self,marca):
        self.marca = marca

    def __str__(self) -> str:
        return f'Bebida - identificador:{self.identificador} - cantidadLitros:{self.identificador} - precio:{self.precio} - marca:{self.marca}'