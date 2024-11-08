notas = int(input("ingrese la nota "))

if (notas >= 0 and notas <= 5):
    print(f"suspende {notas}")
elif(notas >5 and notas <= 6):
    print(f"aprobado {notas}")
elif(notas >6 and notas <= 7):
    print(f"bien {notas}")
elif(notas >7 and notas <= 9):
    print(f"notable {notas}")
elif(notas >9 and notas <= 10):
    print(f"sobresaliente {notas}")
else:
    print("la nota debe ser del 1 al 10")