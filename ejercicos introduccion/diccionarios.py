dam1 = {1:"jose", 2: "juan"}
print(type(dam1))

dam1[3] = "maria"#añade al diccionario
print(dam1)

dam2 = {"java":"Jose Manuel","SI":"Javier"}

dam2["python"] = ["jose Manuel"]# añade al diccionario 
print(dam2.setdefault("oracle","BBDD"))#sie el valor no existe lo crea y agrega el valor despues de la coma
print(dam2)
dam2.pop("SI")#elimina el valor donde la clave sea arduino
dam2.popitem()

if(  "java" in dam1):
    print("si existe")
else:
    print("no existe")
print(dam2["python"])
print(dam2.get("arduino","No hay profesore"))#pregunta por una variable o devuelve el valor despues de la coma

#items,keys,values

for i,v in dam1.items():#imptimir calve y valor
    print(i,v)

for c in dam1.keys():#imprime clave y valor a partir de las claves 
    print(c,dam1[c])

for v in dam1.values():#imprime los valores pero no las claves
    print(v)


dam2 = {"java":"Jose Manuel","SI":"Javier" ,"SI2":"Francisco Javier"}
dam1.update(dam2)

print(dam1)