n = int(input("Ingrese la altura de la piramide: "))
s = str(input("Ingrese el simbolo para la piramide: "))
for i in range(0,n,1):
    print((" ")*(n-i) + (s * i)+ (s * (i-1)))
