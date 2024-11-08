def cocienteResto(numerador,denominador):
    c=0
    while(numerador>=denominador):
        numerador-=denominador
        c+=1
    return(c,numerador)
tupla = cocienteResto(7,2)
print(f"cociente = {tupla[0]} resto={tupla[1]}")