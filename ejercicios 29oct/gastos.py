
gastos = {}

seguir = "si"

while (seguir == "si"):
    gasto = str(input("ingrese el origen del gasto "))

    if (gasto in gastos):
        cantidad = int(input("ingrese el valor del gasto "))
        gastos[gasto] += cantidad
    else:
        gastos[gasto] = 0
        cantidad = int(input("ingrese el valor del gasto "))
        gastos[gasto] += cantidad

    print(gastos)

    seguir = str(input("Desea Seguir? "))


print(gastos)

gastos1 = {}
while True:
    concepto = input("dime el concepto del gasto")
    importe =float(input("dime el gasto"))
    if (concepto in gastos1):
        gastos[concepto] +=importe
    else:
        gastos[concepto] = importe
    
    continuar = str(input("desea continuar?"))

    if(continuar == "no"):
        break

print(gastos1)