diccionario = {"jose":30,"juan":40,"ana":20}

diccionario_ordenado = dict(sorted(diccionario.items(),reverse=True))

print(diccionario_ordenado)

diccionario_ordenado1 = dict(sorted(diccionario.items(), key = lambda item:item[0]))

print(diccionario_ordenado1)