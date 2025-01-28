from Punto import Punto as pt;
from Rectangulo import Rectangulo as rect;


print(pt.nptos)
p1 = pt()
print(p1)
print(pt.nptos)
p2 = p1.clonar()
p3 = pt(8,0)
p3.nptos = 12
print (p2)
print (p3)

rectangulo = rect(10,20,pt(2,2))
print(rectangulo)
rectangulo1 = rect(10,20,p3)

print(rectangulo1)
p3.trasladar(-8,8)
print(rectangulo1)
rectangulo4 = rect(2,2)
print(rectangulo4)
print(rectangulo1.area())