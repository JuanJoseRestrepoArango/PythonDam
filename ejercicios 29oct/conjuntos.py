conjunto = {"marta","luis","juan"}

print(len(conjunto), type(conjunto))

for i in conjunto: 
    print(i)

if ("ana" in conjunto ):
    print("si esta")

conjunto.add("ana")

conjunto.remove("ana")#si no existe  da error

conjunto.discard("pepe") #si no existe no da error

conjunto2 = {"maria","luis","ana"}
conjunto.update(conjunto2)
print(conjunto)

conjunto.pop() #elimina el ultimo elemento