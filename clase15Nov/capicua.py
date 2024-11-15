
def capicua(n):
    rev = ""
    for i in range(len(num)-1,-1,-1):
        rev = rev + num[i]

    return rev == num
def intCapicua(n):
    rev= 0
    sobra = 0
    c = n
    while(n>0):
        sobra = n %10
        n = n//10
        rev = rev*10+sobra
    return rev == c

num = input("Ingrese un numero ")
if(intCapicua(int(num))):
    print("Es capicua")
else:
    print("no es capicua")


