import os
def menu(): 
    os.system("cls")  
    global sabores
    s = str (input(f"Elija un sabor ({sabores[1]}, {sabores[2]} o {sabores[3]}): "))
    return s

def tipo():
    os.system("cls")
    global tipos
    t = str (input(f"¿Qué tipo de chocolate quiere? ({tipos[1]} o {tipos[2]}): "))
    return t
def imprimir(s,t,n,nom,ps):
    os.system("cls")  
    global sabores
    global tipos
    global precios
    if (s == sabores[3]):
        print(f"Tarta de {s} {t}: {precios[s]+precios[t]} €")
    else:
        print(f"Tarta de {s}: {precios[s]} €")
    if (n == "si"):print("Con nata: 2,50 €")
    if (nom == "si"):print("Con nombre: 2,75 €")
    print(f"Total: {ps}€")
    

if __name__ == "__main__":
    sabores= {1:"manzana",2:"fresa",3:"chocolate"} 
    precios= {"manzana":18.00,"fresa":16.00,"chocolate":14.00,"blanco":1,"negro":0} 
    tipos = {1:"blanco",2:"negro"}
    start = "s"
    while(start == "s"):
        s = menu()
        ps = precios[s]
        if(s == sabores[3]):
            t = tipo()
            if(t == tipos[1]):ps = precios[s]+1
        else:
            t = ""
        
         
        while(True):
            n  = input("¿Quiere nata? (si o no): ")
            if (n == "si"): 
                ps = ps +2.50
                break
            elif (n == "no"):
                break
            else:
                print("Respuesta no valida")
        while(True):
            nom = input("¿Quiere ponerle un nombre? (si o no): ")
            if (nom == "si"): 
                ps = ps +2.75
                break
            elif (nom == "no"):
                break
            else:
                print("Respuesta no valida")


        imprimir(s,t,n,nom,ps)
        while(True):
            start = str(input("¿Quiere Continuar? (s/n): "))
            if(start != "s" and start != "n"):
                print("Debe responder con s o n")
            else:
                break
        
        