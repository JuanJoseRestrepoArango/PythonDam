def primo(n):
    for i in range(2,int(n)-1):
        if(n%i==0):
            return False
    return True

n1 = int(input("ingrese el numero a analizar "))

if(primo(n1)):
    print(f"es numero primo {n1}")
else:
    print(f"el numero no es primo {n1}")

