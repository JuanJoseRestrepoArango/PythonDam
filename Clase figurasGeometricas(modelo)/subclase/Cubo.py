from clases.Cuadrado import Cuadrado

class Cubo(Cuadrado):
    def perimetro(self):
        return 12*self.lado1
    def area(self):
        return 6*super().area()
    def volumen(self):
        return pow(self.lado1,3)
    def __str__(self):
        return f'Cubo lados = {self.lado1}'