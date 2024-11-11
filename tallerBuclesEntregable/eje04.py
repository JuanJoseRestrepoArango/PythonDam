num1 = str(input("Ingrese el primer numero "))
num2 = str(input("Ingrese el segundo numero "))
par = ""
impar = ""
if (len(num2)>len(num1)):
    l = len(num2)
else:
    l = len(num1)

for i in range(0,l,1):
    if(int(num1[i])%2 == 0):
        par = par + num1[i]
    if (int(num2[i])%2 == 0):
        par = par + num2[i]
print(par)

for i in range(0,l,1):
    if(int(num1[i])%2 != 0):
        impar = impar + num1[i]
    if (int(num2[i])%2 != 0):
        impar = impar + num2[i]
print(impar)