letra = "TRWAGMYFPDXBNJZSQVHLCKE"

def identificacion(ide):
    primer = ide[0:1]
    n = "XYZ".find(primer)
    
    if(n>=0):
        numero = int(str(n)+ide[1:])
    else:
        numero = int(ide)

    resto = numero % 23
    return letra[resto:resto+1]
    
#finde devuelve -1 en caso de que n encuentre

if __name__ == "__main__":
    dniNie = str(input("ingrese su dni/nie "))
    print(identificacion(dniNie))