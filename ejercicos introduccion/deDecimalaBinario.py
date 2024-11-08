cadena = str(input("ingrese el binario "))
n = len(cadena)-1
suma=0
for i in cadena:
    suma =suma+(int(i)*pow(2,n))
    n = n+1
print(suma)