
def capicua(n:str):
    rev = ""
    for i in range(len(n)-1,-1,-1):
        rev = rev + n[i]

    return rev == n
def iscapicua(n:int):
    rev= 0
    sobra = 0
    c = n
    while(n>0):
        sobra = n %10
        n = n//10
        rev = rev*10+sobra
    return rev == c

if __name__ == "__main__":
    num = input("Ingrese un numero ")
    if(capicua(num)):
        print("Es capicua")
    else:
        print("no es capicua")
    if(iscapicua(int(num))):
        print("Es capicua")
    else:
        print("no es capicua")



