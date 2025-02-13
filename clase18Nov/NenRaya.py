import numpy as np
import os

def rellenarSolucion(m):
    nf = len(m)
    nc = len(m[0])
    c = 0
    for i in range(0,nc,1):
        m[nf-2][i] = (i*nc)+(i+1)
        m[nf-1][i] = (i*nc)+(nc-i)
        for j in range(0,nc,1):
            m[c][j] = (i*nc)+(j+1)
            m[c+nc][j]=(j*nc)+(i+1)
        c+=1

def rellenarMov(m):
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            m[i][j] = "-"

def imprimir (m):
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            print(f"{m[i][j]:3}",end=" ")
        print()

def tablero (nc):
    for i in range(0,nc,1):
        for j in range(0,nc,1):
            print(f"{((i*nc)+(j+1)):3}",end=" ")
        print()

def imprimirMov (m):
    print()
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            print(f"{m[i][j]:3}",end=" ")
        print()

def tirar(m,jug):
    while True:
        pos = int(input("Dime la posicion "))
        if not(pos>=1 and pos<=len(m)*len(m)):continue
        nc = (pos-1)%len(m)
        nf = (pos-1)//len(m)
        if(m[nf][nc] == "-"):
            if(jug):
                m[nf][nc] = "X"
                break
            else:
                m[nf][nc] = "O"
                break
        else:
            print("La posicion ya esta seleccionada")

def comprobar(jug,mov,sol):
    cadena = "X" if (jug) else "O"
    for i in range(0,len(sol),1):
        aciertos = 0
        for j in range(0,len(sol[i]),1):
            m = sol[i][j]
            c = (m-1)%len(sol[i])
            f = int((m-1)//len(sol[i]))
            if(mov[f][c] == cadena):
                aciertos+=1
        if(aciertos == len(sol[i])):
            return True
    return False

def menu(mov,n,jug):
    os.system("cls")
    opciones = {1:"Ver Posiciones", 2:"Ver Movimientos", 3:"Tirar", 4:"Salir"}
    while(True):
        print("Juega 1" if (jug) else "Juega 2")
        for v,k in opciones.items():
            print(v,k)  
        opcion = int(input("Ingrese el numero de la opcion: "))
        if(opcion == 1):
            tablero(n)
        elif(opcion == 2):
            imprimirMov(mov)
        elif(opcion == 3):
            tirar(mov,jug)
            break
        elif(opcion == 4):
            return True
            break
        else:
            print("Debe seleccionar una opcion valida")
    return False
        
    
    


if __name__ == "__main__":
    jug = True
    n = int(input("Dime el nº de filas /columnas "))
    nSol = (n*2)+2
    j1 = 0
    j2 = 0
    mov = np.zeros((n,n),dtype=str)
    sol = np.zeros((nSol,n),dtype=int)
    rellenarSolucion(sol)
    rellenarMov(mov)
    while True:
          
        s = menu(mov,n,jug)
        if(s):break
        if (jug):
            j1+=1 
        else:
            j2+=1
        if(j1>=n or j2>=n):
            if(comprobar(jug,mov,sol)):
                print("Gano el " + ("jugador 1" if (jug) else "jugador 2"))
                imprimirMov(mov)
                break
        if(j1+j2 == n*n):
            print("Empate")
            break
        jug = not(jug)
