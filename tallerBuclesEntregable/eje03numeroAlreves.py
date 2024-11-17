def revstr(n:str):
    rev = ""
    for i in range(len(n)-1,-1,-1):
        rev = rev + n[i:i+1]

    return rev
def revint(n:int):
    rev= 0
    sobra = 0
    c = n
    while(n>0):
        sobra = n %10
        n = n//10
        rev = rev*10+sobra
    return rev 




num = str(input("Ingrese un numero: "))

print(revstr(num))
print(revint(int(num)))