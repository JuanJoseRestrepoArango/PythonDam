lstEng=[]#lista en ingles
lstEsp=[]#lista en español

seguir = "si"
while(seguir != "no"):
    palabra = input("Ingrese la palabra en ingles ")
    lstEng.append(palabra)

    if palabra in lstEng:
        palabraEsp = input("Ingrese la traduccion al español ")
        lstEsp.append(palabraEsp)
    else:
        palabra = input("Ingrese la palabra en ingles ")
        lstEng.append(palabra)

    print(f'Palabras en ingles{lstEng},Palabras en español {lstEsp}')

    seguir = input("Desea seguir? ")

print("Proceso Terminado")