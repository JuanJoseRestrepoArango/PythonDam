from enum import Enum

class Meses(Enum):
    ENERO = ('ENero', 31,)
    FEBRERO = ('Febrero',28,)

class Consumo(Enum):
    A = 100
    B = 80
    C = 60
    D = 50
    E = 30
    F = 10
class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    AZUL = 4
    GRIS = 5

def comprobar(co):
    for i in Consumo:
        if co == i.name: return i
    return Consumo.A

a = "B"
a= comprobar(a)
print(a.name, a.value)

for i in Meses:
    print(i.name, i.value)
for i in Meses.__members__:
    print(i)