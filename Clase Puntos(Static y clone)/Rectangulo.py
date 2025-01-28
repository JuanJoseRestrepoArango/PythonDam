from Punto import Punto as pt

class Rectangulo:

    def __init__(self, ancho,alto,origen = pt()):
        self.ancho = ancho
        self.alto = alto
        self.origen = origen

    def getAncho(self):
        return self.ancho
    def getAlto(self):
        return self.alto
    def __str__(self) -> str:
        return f'Rectangulo [ancho = {self.ancho}, alto = {self.alto}, origen = {self.origen}'
    def area(self):
        return f'Area = {self.alto * self.ancho}'
