l = ["suspenso","aprobado","Bien", "notable", "sobresaliente"]
b = [3,5,3,0,10,7]
cali =[]
for i in b:
    if (i<=5): 
        cali.append(l[0])
    elif(i<=6):
         cali.append(l[1])
    elif(i<=7):
         cali.append(l[2])
    elif(i<=9):
         cali.append(l[3])
    elif(i<=10):
         cali.append(l[4])
print(cali)

for j,v in enumerate(cali):
    print("indice = {} y calificacion = {}".format(j,v))