t = 0 
e = ""
start = "s"
while(start == "s"):
    while(t == 0):
        h = int (input("Introduzca la altura de la bandera en cm: "))
        a = int (input("Ahora introduzca la anchura: "))
        if (a > 0 and h > 0):
            t = h * a
        else:
            print("Introduzca valores mayores a 0")
    while(e != "s" and e != "n"):
        e = str(input("¿Quiere escudo bordado? (s/n): "))
        if(e != "s" and e != "n"):
            print("Debe responder con s o n")
    print("Gracias. Aquí tiene el desglose de su compra.") 
    print(f"Bandera de {t}cm2: {t*0.01}€")  
    if(e=="s"):
        e = "Con Escudo"
        es = 2.50
    else:
        e = "Sin Escudo"
        es = 0
    print(f"{e}: {es}€")  
    print(f"Gastos de envío: {3.25}€")  
    print(f"Bandera de {t}cm2: {(t*0.01)+es+3.25}€") 
    while(True):
        start = str(input("¿Quiere Continuar? (s/n): "))
        if(start != "s" and start != "n"):
            print("Debe responder con s o n")
        else:
            break
    t = 0 
    e = ""
    

        