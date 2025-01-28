from claseAbstractas.figuraGeometrica import figuraGeometrica;

class Rectangulo(figuraGeometrica):
    
    def __init__(self, lado1,lado2):
        super().__init__(lado1)
        self.lado2 = lado2

    def perimetro(self):
        return 2* (self.lado1+self.lado2)
    def area(self):
        return self.lado1 * self.lado2
    def __str__(self):
        return f'Rectangulo Lado2 = {self.lado2} '+super().__str__()

    