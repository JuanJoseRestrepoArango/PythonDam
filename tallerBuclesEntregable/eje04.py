num1 = str(input("Por favor, introduzca un número: "))
num2 = str(input("Introduzca otro número: "))
par = ""
impar = ""
if (len(num2)>len(num1)):
    l = len(num2)
else:
    l = len(num1)

for i in range(0,l,1):
    if(len(num1)-1>=i):
        if(int(num1[i])%2 == 0):
            par = par + num1[i]
    if(len(num2)-1>=i):
        if (int(num2[i])%2 == 0):
            par = par + num2[i]


for i in range(0,l,1):
    if(len(num1)-1>=i):
        if(int(num1[i])%2 != 0):
            impar = impar + num1[i]
    if(len(num2)-1>=i):
        if (int(num2[i])%2 != 0):
            impar = impar + num2[i]
print(f"El número formado por los dígitos pares es {par}")
print(f"El número formado por los dígitos impares es {impar}")
