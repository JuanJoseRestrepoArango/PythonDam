def bisiesto(anno:int):
     return (((anno%4==0)and(anno%100!=0)) or (anno%400==0)) 

mes = int(input("Dime el numero de mes "))

match mes:
    case 1|3|5|7|8|10|12:
        ndias = 31
    case 2: 
        a = int(input("Dime el año "))
        #ndias = 29 if (((a%4==0)and(a%100!=0)) or (a%400==0)) else 28
        if bisiesto(a)==True:
            ndias=29
        else:
            ndias = 28
    case _:
        ndias=30

print(ndias)
print(f"el numero de dias {mes} es {ndias}")