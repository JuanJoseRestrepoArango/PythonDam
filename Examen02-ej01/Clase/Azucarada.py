from ClaseAbstracta.Bebida import Bebida

class Azucarada(Bebida):
    def __init__(self, identificador, cantidadLitros, precio, marca,porAzucar,promocion):
        super().__init__(identificador, cantidadLitros, precio, marca)
        self.porAzucar = porAzucar
        self.promocion = promocion


    def getPorAzucar(self):
        return self.porAzucar
    
    def setPorAzucar(self, porAzucar):
        self.porAzucar = porAzucar
    def getpromocion(self):
        return self.promocion
    
    def setpromocion(self, promocion):
        self.promocion = promocion

    def VerificarPromocion(self):
        if self.promocion :
            self.precio = self.precio - (self.precio * 0.10)

    def __str__(self) -> str:
        return super().__str__()+ f'- porcentajeAzucar:{self.porAzucar} - promocion:{self.promocion}' 