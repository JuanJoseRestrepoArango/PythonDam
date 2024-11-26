import numpy as np;
import random
import os

def rellenar(m,li,ls):
    os.system("cls")
    for i in range(0,len(m),1):
        for j in range(0,len(m[i]),1):
            m[i][j] = random.randint(li,ls)

def imprimir(m,p,res):

    print(" "*65,end="")
    for i in range(0,len(res),1):
        print(f"{res[i]:6} ", end=" ")
    print()
    for i in range(0,len(m),1):
        vmax = m[i][0]
        vmin = m[i][0]
        med = 0
        print(f"{p[i]:10}",end=" ")
        for j in range(0,len(m[i]),1):
            if(vmax<=m[i][j]):vmax = m[i][j]
            elif(vmin>=m[i][j]):vmin = m[i][j]
            med+=m[i][j]
            print(f"{m[i][j]:4}",end=" ")
        print(f"{" "*4}{round((med/len(m[i])),1):4}, {vmin:5}, {vmax:4},")
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
    nf = 4
    nc = 10
    li = 140
    ls = 210
    m = np.zeros([nf,nc],dtype= int)
    p =  ["España", "Rusia", "Japón","Australia"]
    res =  ["Media", "Min", "Max"]
    rellenar(m,li,ls)
    imprimir(m,p,res)
    
