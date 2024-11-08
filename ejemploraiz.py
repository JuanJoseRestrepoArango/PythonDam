import math

a= int(input("Ingrese el valor de a"))
b= int(input("Ingrese el valor de b"))
c= int(input("Ingrese el valor de c"))

radicando = pow(b,2)-(4*a*c)

if radicando >=0:
    raiz1 =(-b+math.sqrt(radicando))/(2*a)
    raiz2 =(-b-math.sqrt(radicando))/(2*a)
    print(f'{a}*x^2+{b}*x+{c} tiene las raicas {raiz1} {raiz2}')
else:
    print('no tiene raiz real')