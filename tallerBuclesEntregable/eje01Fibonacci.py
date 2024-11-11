
n = int(input("Ingrese el numero de los terminos de la sucesion de fibonacci que quiere ver "))
res = 0
num  = [0,1]

for i in range(0,n):
    if(i == 0 ):
        print(num[0])
    elif(i == 1 ):
        print(num[1])
    else:
        res = num[i-1]+num[i-2]
        num.append(res) 
        print(num[i])
    