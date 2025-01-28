from claseAbstractas.figuraGeometrica import figuraGeometrica;

class Cuadrado(figuraGeometrica):
    def perimetro(self):
        return 4* self.lado1
    def area(self):
        return pow(self.lado1,2)
    def __str__(self):
        return f'Cuadrado Lado = {self.lado1}'