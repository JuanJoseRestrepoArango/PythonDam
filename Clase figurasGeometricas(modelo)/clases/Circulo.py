from claseAbstractas.figuraGeometrica import figuraGeometrica
import math
class Circulo(figuraGeometrica):
    def perimetro(self):
        return 2* math.pi *self.lado1
    def area(self):
        return math.pi *(pow(self.lado1,2))
    