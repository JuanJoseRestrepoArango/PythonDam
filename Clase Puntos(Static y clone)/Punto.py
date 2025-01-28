import copy
class Punto:
    nptos = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Punto.nptos +=1
    def __str__(self) -> str:
        return f'Punto x={self.x} Punto y ={self.y} Npuntos Clase = {Punto.nptos} Npuntos Instancia = {self.nptos}'
    def setPuntosX(self, x):
        self.x = x
    def setPuntosY(self, y):
        self.y = y

    def trasladar(self,x,y):
        self.x += x
        self.y += y

    def clonar(self):
        Punto.nptos += 1
        return copy.deepcopy(self)
