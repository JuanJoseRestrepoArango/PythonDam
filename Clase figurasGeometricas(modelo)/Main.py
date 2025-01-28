from clases.Cuadrado import Cuadrado;
from clases.Rectangulo import Rectangulo;
from clases.Circulo import Circulo;
from subclase.Cubo import Cubo;


def imprimir(li):
    for i in li:
        print(i.__str__(),i.perimetro(),i.area())
def contar(li):
    lista = [["cubo",0],["Rectangulo",0],["Circulo",0],["Cuadrado",0]]
    for i in li:
        if isinstance(i,Cubo):
            n=0
        elif isinstance(i,Rectangulo):
            n=1
        elif isinstance(i,Circulo):
            n=2
        elif isinstance(i,Cuadrado):
            n=3
        lista[n][1] += 1 
    for i in lista:
        print(i)
lista = []
lista.append(Cuadrado(10))
lista.append(Cubo(10))
lista.append(Cubo(10))
lista.append(Cubo(10))
lista.append(Rectangulo(10,20))
lista.append(Rectangulo(10,20))

lista.append(Circulo(5))
imprimir(lista)
contar(lista)