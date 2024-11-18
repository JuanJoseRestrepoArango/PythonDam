import numpy as np

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
        pos = int(input("Dime la posicion"))
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
        while True:
            print("Juega 1" if (jug) else "Juega 2")
            break
        tablero(n)
        tirar(mov,jug)
        imprimirMov(mov)
        if (jug):
            j1+=1 
        else:
            j2+=1
        if(j1>=n or j2>=n):
            if(comprobar(jug,mov,sol)):
                print("Gano el jugador" + ("jugador 1" if (jug) else "jugador 2"))
                break
        if(j1+j2 == n*n):
            print("Empate")
            break
        jug = not(jug)
