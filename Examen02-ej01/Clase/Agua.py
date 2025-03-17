from ClaseAbstracta.Bebida import Bebida

class Agua(Bebida):
    def __init__(self, identificador, cantidadLitros, precio, marca,origen):
        super().__init__(identificador, cantidadLitros, precio, marca)
        self.origen = origen


    def getOrigen(self):
        return self.origen
    
    def setOrigen(self, origen):
        self.origen = origen

    def __str__(self) -> str:
        return super().__str__() + f'- origen:{self.origen}'