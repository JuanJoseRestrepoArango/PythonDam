b = float(input("Ingrese un valor para la base "))
e = int(input("Ingrese un valor para el exponente "))

resultado=1
for i in range(e):
    resultado = resultado*b
print(f"el resultado del es {resultado}")