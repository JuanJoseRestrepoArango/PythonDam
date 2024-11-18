import numpy as np;
import random

def rellenar(m,li,ls):
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            m[i][j] = random.randint(li,ls)

def imprimir(m):
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            print(f"{m[i][j]:4}",end=" ")
        print()
    print()

def rotar(m,r):
    c = len(m)/2
    for i in range(0,len(m),1):
        t = len(m)-1-i

        for j in range(i,t,1):
            r[i][j+1] = m[i][j]
            r[j+1][t] = m[j][t]
            r[t][t+i-j-1] = m [t][t+i-j]
            r[t+i-j-1][i] = m[t+i-j][i]


if __name__ == "__main__":
    nf = 12
    nc = 12
    li = 0
    ls = 100
    m = np.zeros([nf,nc],dtype= int)
    r = np.zeros([nf,nc],dtype= int)
    rellenar(m,li,ls)
    imprimir(m)
    rotar(m,r)
    imprimir(r)
