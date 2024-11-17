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
def imprimir(s,t,b,ps):
    os.system("cls")  
    global sabores
    global tipos
    global bebidas
    global precios
    if (s == sabores[3]):
        print(f"{s} en {t}: {precios[s]+precios[t]} €".capitalize())
    else:
        print(f"{s}: {precios[s]} €".capitalize())
    print(f"{b}: {precios[b]}".capitalize())
    print(f"Total desayuno: {round(ps,2)} €")
    

if __name__ == "__main__":
    sabores= {1:"palmera",2:"donut",3:"pitufo"} 
    bebidas= {1:"zumo",2:"cafe"} 
    precios= {"palmera":1.40,"donut":1.00,"pitufo":1.20,"tortilla":0.40,"aceite":0,"zumo":1.50, "cafe" :1.20} 
    tipos = {1:"aceite",2:"tortilla"}
    start = "s"
    while(start == "s"):
        while(True):
            s = menu()
            if(s in sabores.values()):
                break
            else:
                print("Debe seleccionar un producto de la lista")
        ps = precios[s]
        if(s == sabores[3]):
            while(True):
                t = tipo()
                if t in tipos.values() :break
            if(t == tipos[1]):ps = precios[s]+1
        else:
            t = ""
        
        while(True): 
            b = bebida()
            if b in bebidas.values():break
        ps = ps +precios[b]
            

        imprimir(s,t,b,ps)
        while(True):
            start = str(input("¿Quiere Continuar? (s/n): "))
            if(start != "s" and start != "n"):
                print("Debe responder con s o n")
            else:
                break
        
        