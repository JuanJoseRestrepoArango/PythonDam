numero = int(input('dime el numer decimal'))
v = numero
binario = ""

while (numero !=0 ):
    resto = numero%2
    numero = numero //2 # // division entera
    binario = binario + str(resto)

print(f'el binario de {v} es {binario}')