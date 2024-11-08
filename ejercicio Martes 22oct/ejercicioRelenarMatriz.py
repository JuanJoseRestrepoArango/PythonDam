import numpy as np

def  imprimir(matriz): 
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(f'{matriz[fila][columna]: 3d}', end = ' ')
        print()
            
def rellenar(matriz):
    global f,c
    for n in range(1,f*c+1):
        fila = (n-1)//c
        columna = n-(fila*c)-1
        numero = int(input(f'Dime la posicion {fila}:{columna} '))
        matriz[fila][columna] = numero
def buscar(matriz):
    numBus = int(input('Ingrese el numero a buscar '))
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if numBus == matriz[fila][columna]:
                print(f'El numero esta ubicado en la fila{fila} y en la columna {columna}')

if __name__ == '__main__':
    f = int(input('Ingrese el numero de filas '))
    c = int(input('Ingrese el numero de columnas '))
    matriz = np.zeros([f,c],dtype=int)
    rellenar(matriz)
    imprimir(matriz)
    # asi se comenta en python __name__ == '__main__' es para saber donde se inicia