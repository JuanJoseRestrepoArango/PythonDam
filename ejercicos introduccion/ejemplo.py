numero = int(input("Dime un numero entero"))

if(numero%2==0):
    print("par ")
else:
    print("impar ")

x = "par" if numero%2==0 else "impar" #operador termnario 
print(x)