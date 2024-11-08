lista = ["hola", 12,33,44,123,45]
print(type(lista))
print( lista)

lista.append(12)
lista.append(13)
lista.append(17)
lista.append(21)

print (lista, len(lista))

for i in lista : 
    print(i)

for j,v in enumerate(lista):
    print("indice = {} y valores = {}".format(j,v))

for x in range(len(lista)):
    print("indice = {} y valores = {}".format(x,lista[x]))

