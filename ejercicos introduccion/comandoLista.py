#La lista es una colección ordenada y modificable. Permite miembros duplicados.

# – lst.append(item): Añade un ítem al final de la lista:
# – lst.extend(lst2): Une una lista a otra
# – lst.insert(index, item): insert the given item before the index and return None.
#   lst.insert(0, item) inserts before the #first item of the
#   lst.insert(len(lst), item) inserts at the end of the lst which is the same as lst.append(item).
# – lst.index(item): Devuelve el índice en el que aparece un ítem (error si no aparece):
# – lst.remove(item): remove the first occurrence of item from the lst and return None; or error.
# – lst.pop(): Extrae un ítem de la lista y lo borra:
# – lst.pop(index): Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):
# – lst.clear(): Vacía todos los ítems de una lista:
# – lst.count(item): Cuenta el número de veces que aparece un ítem:
# – lst.reverse(): Le da la vuelta a la lista actual:
# – lst.sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor
# – lst.sort(reverse=True): Ordena automáticamente los ítems de una lista por su valor de mayor a mayor

# – lst.copy(): return a copy of lst; same as lst[:].


lst=[]
print(type(lst))

lst.append(10)
lst.append([1,2,3])
lst.append(30)


for i,v in enumerate(lst):#i,v enumerate para poder ver posicion y valor de a lista
    print(i,v)

lst.extend(["a","b","c"])#extend une una ista con otra

lst.insert(3,"hola")#insetrto un valor (posicion,valor)
lst.insert(len(lst),[1,2,3,4])#insetrto un valor (posicion,valor)

print(lst)

if 30 in lst:
    
    print("esta en la lista",lst.index(30))
else:
    
    print("no esta en la lista")