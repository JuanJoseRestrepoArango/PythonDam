def sinRepetir(a):
    b = []
    for i in range(0,len(a),1):
        if(a[i] in b):
            continue
        else:
            b.append(a[i])
    return b
def imprimir(m):
    for i in range(0,len(m),1):
        print(f"{m[i]:8}",end=" ")


if __name__ == "__main__":
    a = ["casa","coche","sol","mesa","mesa","coche","ordenador","sol","CASA"]
    imprimir(a)
    print()
    b = sinRepetir(a)
    imprimir(b)