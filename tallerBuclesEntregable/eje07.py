import os
def menu(): 
    os.system("cls")  
    global sabores
    # for k,v in sabores.items():
    #     print(k, v) 
    s = str (input(f"¿Qué ha tomado de comer? ({sabores[1]}, {sabores[2]} o {sabores[3]}): "))
    return s

def tipo():
    os.system("cls")
    global tipos
    t = str (input(f"¿Qué tipo quiere? ({tipos[1]} o {tipos[2]}): "))
    return t
def bebida():
    os.system("cls")
    global bebidas
    t = str (input(f"¿Qué ha tomado de beber? ({bebidas[1]} o {bebidas[2]}): "))
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
    print(f"Total: {ps}")
    

if __name__ == "__main__":
    sabores= {1:"palmera",2:"fresa",3:"chocolate"} 
    bebidas= {1:"zumo",2:"café"} 
    precios= {"manzana":1.40,"donut":1.00,"pitufo":1.20,"tortilla":0.40,"aceite":0,"zumo":1.50, "cafe" :1.20} 
    tipos = {1:"aceite",2:"tortilla"}
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
        
        