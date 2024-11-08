suma = 0
cont = 0
while(True):
    n1 = float(input("Ingrese un numero "))
    
    if(n1<=0):
        break
    else:
        suma = suma +n1
    cont = cont +1
print(f"suma {suma} , contador {cont}")