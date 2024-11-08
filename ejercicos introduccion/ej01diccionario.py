#pedir la palabra en español y  revisar si existe ene l diccionario de no ser asi debe agregarse la palabra y su traduccion al diccionario
dicEsp = {}


opcion = "no"

while(opcion == "no"):
    print(dicEsp)
    palabraEsp = input("Ingrese una palabra en español ")
    if (palabraEsp in dicEsp):
        print(palabraEsp,dicEsp[palabraEsp])  
    else:
        palabraIng = input("ingrese una palabra en ingles ")
        dicEsp[palabraEsp]=palabraIng
    opcion = input("Desea Salir del programa? ")
print(dicEsp)