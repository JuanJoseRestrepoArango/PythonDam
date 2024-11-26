import numpy as np
import random

def rellenar (m):
    for i in range(0,len(m),1):
        for  j in range(0,len(m[i]),1):
            m[i][j] = random.randint(0,10)


def imprimir(m,al,t):
    print(f"{" "*15}",end="")
    for i in range(0,len(t),1):
        print(t[i],end="   ")
    print()
    pC = [0,0,0]
    for i in range(0,len(m),1):
        pF = 0
        print(al[i],end="")
        for  j in range(0,len(m[i]),1):
            pC[j] = pC[j]+m[i][j]
            pF = pF + m[i][j]
            print(f"{m[i][j]:10}",end="")
        #print(f"{round(pF/len(m[i]),2):10}\n")
        print()
    print("Prom-Tri",end="")
    for i in range(0,len(pC),1):
        print(f"{round((pC[i]/len(m)),2):10}",end="")

def promAl(m,t):
    N = int(input("\nIngrese la posicion del alumno para ver su promedio "))-1
    for i in range(0,len(m),1):
        pF = 0
        for  j in range(0,len(m[i]),1):
            pF = pF + m[N][j]
    print(f"El Alumno {N+1} tiene de promedio {round(pF/(len(t)),2)}")
            
        

if __name__ == "__main__":
    m = np.zeros([5,3],dtype= int)
    al = ["Alumno 1","Alumno 2","Alumno 3","Alumno 4","Alumno 5"]
    t = ["Primer","Segundo","Tercer"]
    rellenar(m)
    imprimir(m,al,t)
    r = "s"
    while(r == "s"):
        promAl(m,t)
        r = input("Desea Continuar?(s/n) ")
        
    