import os

def dec_bin(n):
    numero = n.split("/")
    valores = numero[0].split(".")
    cadena = ""
    sumarizacion = ""
    resultado = []
    cont = int(numero[1])
    
    for i in valores:
        binario = ""
        n = int(i)
        while n > 0:
            r = n % 2
            n = n//2
            binario = str(r)+binario

        binario = (8-len(binario)) * "0" +binario
        if(int(i) == int(valores[-1])):
            cadena = cadena + binario 
        else:
            cadena = cadena + binario + "."


    resultado.append(cadena)
    

    for i in range(0,32+3,1):
        if(cadena[i] != "." and cont > 0):
            sumarizacion = sumarizacion + "1" 
            cont -= 1
        elif(cadena[i] == "."):
            sumarizacion = sumarizacion + "."
        else:
            sumarizacion = sumarizacion + "0"
        
    resultado.append(sumarizacion)
    bin_dec(resultado)

    return resultado
def bin_dec(lista):
    resultado = []
    ipes = ""
    mascaras = ""
    ip = lista[0].split(".")
    for i in ip:
        n = len(i)-1
        suma = 0
        for l in i:
            suma = suma+(int(l)*pow(2,n))
            n = n-1
        if(i!= ip[-1]):
            ipes = ipes +str(suma) + "."
        else:
            ipes = ipes +str(suma) 
        
        
    resultado.append(ipes)
    mascara = lista[1].split(".")
    for i in mascara:
        n = len(i)-1
        suma = 0
        for l in i:
            suma = suma+(int(l)*pow(2,n))
            n = n-1
        if(i!= mascara[-1]):
            mascaras = mascaras +str(suma) + "."
        else:
            mascaras = mascaras +str(suma)
        
    resultado.append(mascaras)
    print(resultado)
    

def imprimirBinarios(lista):
    for i in lista:
        print(i)



if __name__ == "__main__":
    lista = ["10.56.248.0/24","10.56.249.0/25","10.56.249.128/26","10.56.249.192/26","10.56.250.0/23"]
    listaBinarios = []
    for i in range(0,len(lista),1):
        listaBinarios.append(dec_bin(lista[i]))

    imprimirBinarios(listaBinarios)
    cadena = listaBinarios[0][0]
    
    
    for i in listaBinarios:
        respuesta = ""
        cont = 0
        for j in range(0,len(cadena)):
            
            if(cadena[j] == str(i[0][j])):
                respuesta = respuesta + cadena[j]
                if(cadena[j] != "."):
                    cont +=1
            elif(cadena[j] != str(i[0][j])):
                break

        
    print(respuesta, cont)

    
    
