import os
def dec_bin(n):
    binario = ""
    while(n>0):
        r = n%2
        n = n//2
        binario = str(r)+binario
    return binario

def dec_hex(n):
    lista = ["A","B","C","D","E","F"]
    n = int(n)
    hexadecimal = ""
    while (n>0):
        r = n%16
        n = n//16
        hexadecimal = (str(lista[r -10]) if r>= 10 else str(r)) + hexadecimal
    return hexadecimal


def dec_oct(n):
    octal = ""
    while(n>0):
        r = n%8
        n = n//8
        octal = str(r)+octal
    return octal

def menu(l):
    os.system("cls")
    while True:
        for elem in l :print(elem)
        op = int(input("Ingrese la opcion deseada "))
        if op >= 1 and op <= len(l): return op

def eleccion():
    global base
    while True:
        w = input("Ingrese la base ")
        if (w in base):return w


if __name__ == "__main__":
    lista = ["1.-origen","2.-destino","3.-valor"]
    base = ["dec","bin","hex","oct"]
    continuar = "si"
    funciones = {
        "dec_bin": dec_bin,
        "dec_hex": dec_hex,
        "dec_oct": dec_oct
    }

    while (continuar == "si"):
        # os.system()
        op = menu(lista)
        if(op != 3):
            os.system("cls")
        match op:
            case 1:
                origen = eleccion()
            case 2:
                destino = eleccion()

            case 3:
                valor = input("Dime el valor ")
                print(eval(origen+"_"+destino+"("+valor+")"))
                continuar = input("Desea continuar? ")
                


