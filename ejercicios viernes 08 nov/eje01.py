
def izquierda(n,h):
    c = h
    b = 1
    if(n == 1):
        for i in range(0,h+1,1):    
            print(c*" " + i * "*")
            c = c-1
        for j in range(h-1,0,-1):         
            print(b*" " +j * "*")
            b = b+1
def derecha(n,h):
    if(n == 2):
        for i in range(0,h+1,1):
            print(i * "*")
        for j in range(h-1,0,-1):
            print(j * "*")
def arriba(n,h):
    c = h
    b = -1
    if(n == 3):
        for i in range(0,h+1,1):    
            print(c *" "+ (i+b) * "*")
            b = b+1
            c = c-1

def abajo(n,h):
    c = 0
    b = h-1
    if(n == 4):
        for i in range(h,0,-1):    
            print(c *" "+ (i+b) * "*")
            b = b-1
            c = c+1
def imprimir(opciones):
    for k,v in opciones.items():
        print(v,k)

if __name__ == "__main__":

    opciones = {"izquierda":1,"derecha":2,"arriba":3,"abajo":4}
    h = 4
    seguir = "si"

    while(seguir == "si"):
        imprimir(opciones)
        opcion = str(input("Ingrese la direccion a imprimir "))
        while(True):
            if(opcion not in opciones):
                print("La opcion no esta disponible")
                opcion = str(input("Ingrese la direccion a imprimir "))
            else:
                break
        h = int(input("Ingrese la altura de la piramide "))    
        while(True):
            if(h < 10 and h > 0):
                break
            else:               
                print("La opcion no esta disponible")
                h = int(input("Ingrese la altura de la piramide "))
        n = opciones[opcion]
        derecha(n,h)
        izquierda(n,h)
        arriba(n,h)
        abajo(n,h)
        seguir = str(input("Desea Seguir? "))