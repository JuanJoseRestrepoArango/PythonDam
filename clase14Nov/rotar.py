import numpy as np
import random


def alea(ls,li):
    a = random.randint(li,ls)
    return a

def rellenar(m):
    for i in range(0,len(m)):
        for j in range (0,len(m[i])):
            m[i][j] = alea(100,0)

def imprimir(m):
    for i in range(0,len(m)):
        for j in range (0,len(m[i])):
            print(f"{m[i][j]:5}",end=" ")
        print("\n")
    print("\n")
def rotar (m,r):
    capas = len(m)/2
    for i in range(0,len(m)):
        tope = len(m)-1-i
        for j in range(i,tope):
            r[i][j+1] = m[i][j]
            r[j+1][tope] = m[j][tope]
            r[tope][tope+i-j-1] = m [tope][tope+i-j]
            r[tope+i-j-1][i] = m[tope+i-j][i]

if __name__ == "__main__":
    n = 5
    m = np.zeros([n,n],dtype = int)
    r = np.zeros([n,n],dtype = int)
    c = np.zeros([n,n],dtype = int)

    rellenar(m)
    imprimir(m)
    rotar(m,r)
    imprimir(r)