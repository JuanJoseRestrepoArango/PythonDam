num = str(input("Ingrese un numero: "))

num2 = ""
for i in range(len(num)-1,-1,-1):
    num2 = num2+num[i]
print(num2)