hora = int(input("ingrese la hora "))
frase=["buenos dias","buenas tardes", "buenas noches"]


if (hora>=6 and hora<=12):
    print(frase[0])
elif(hora>=13 and hora<=20):
    print(frase[1])
elif((hora>=21 and hora <=24) or (hora <=5)):
    print(frase[2])
else:
    print("fuera de rango")