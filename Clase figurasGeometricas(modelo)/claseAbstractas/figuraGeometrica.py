from abc import ABC, abstractmethod

class figuraGeometrica(ABC):
    def __init__(self,lado1):
        self.lado1=lado1
    

    def __str__(self):
        return f'FG {self.lado1}'
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass