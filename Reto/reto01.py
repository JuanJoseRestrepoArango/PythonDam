import numpy as np;
import random;

def alea(m,l):
    num = l-1
    letra = random.randint(0,num)
    return m[letra]
def comSec(col,combSec):
    for i in range(0,len(combSec),1):
        combSec[i] = alea(col,len(col))
def combSecSinRep(col,combSec):
    n = ""
    l = ""
    cont = 0
    for i in range(0,len(combSec),1):
        combSec[i] = ""
        n = n +combSec[i]
    print(n)
    while cont < len(combSec):
        l = alea(col,len(col))
        if(n.find(l)<0):
            combSec[cont] = l
            n = n+l
            cont+=1
        
        if (cont == len(combSec)):
            break

def imprimir(m):
    print("\n")
    for i in range(0,len(m),1):
        print(m[i],end="")

def responder(col,resp):
    print("\nOpciones:")
    imprimir(col)
    print("\n")
    cont = 0
    colores = ""
    while(True):
        c = input(f"Ingrese el valor de la respuesta, debe tener {len(resp)} caracteres, ej: {"A"*len(resp)} ")
        if(len(c) == len(resp)):
            break
        else:
            print("El valor ingresado no tiene un tamaño correcto")
    for i in range(0,len(col),1):
        colores  = colores+col[i]
    while(cont<len(resp)):
        for i in range (0,len(resp),1):
            if(colores.find(str(c[i]))>= 0):
                resp[i] = str(c[i])
                cont+=1
            elif(colores.find(str(c[i]))<0):
                print("Debe ingresar una opcion valida")
                c = input("Ingrese el valor de la respuesta")
                print(c)
                i = 0
def evalComb(combSec,resp,avanc,contA):
    cadena = ""
    cadenab = ""
    contB = 0
    for i in range(0,len(combSec),1):
        cadena = cadena+combSec[i]
        avanc[i] = combSec[i]
    for i in range(0,len(resp),1):
        if(avanc[i] == resp[i]):
            resp[i] = "-"
            avanc[i] = resp[i]
    cadena = ""
    for i in range(0,len(avanc),1):
        cadena = cadena+avanc[i]
        if(avanc[i] == "-"):
            contA +=1
    for i in range(0,len(resp),1):
        if(avanc[i] == "-"):
            continue
        elif(cadena.find(resp[i]) >= 0 and cadenab.find(resp[i])<0):
            contB+=1
            cadenab = cadenab+resp[i]
    print(f"\nTiene {contA} aciertos, y {contB} estan en la solucion pero en la posicion incorrecta")




if __name__ == "__main__":
    contA = 0
    contV = 0
    col =["R","A","V","a","M","N","b","B","G","C"]
    nC = int(input("Ingrese el numero de colores de la combinacion "))
    combSec = np.zeros([nC],dtype= str)
    resp = np.zeros([len(combSec)],dtype= str)
    avanc = np.zeros([len(combSec)],dtype= str)
    turnos = 0
    while(True):
        d = input("Quiere que se repitan los numeros? (S/N) ")
        if(d == "S"):
            comSec(col,combSec)
            break
        elif(d == "N"):
            combSecSinRep(col,combSec)
            break
        else:
            print("Debe introducir un valor ")

    while(turnos<=20):
        responder(col,resp)
        print("\nSu respuesta es: ")
        imprimir(resp)
        evalComb(combSec,resp,avanc,contA)
        for i in range (0,len(avanc),1):
            if(avanc[i] == resp[i]):
                contV+=1
        if(contV == len(combSec)):
            print("\nHa Ganado la combinacion secreta es:")
            imprimir(combSec)
            break
        elif(turnos == 20):
            print("\nHas perdido la combinacion es:")
            imprimir(combSec)
            break
        else:
            contV = 0
        

        turnos +=1
        print(f"\nEsta en el turno {turnos}")