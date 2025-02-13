from Class.Lavadora import Lavadora
from Class.Television import Television
from Class.Electrodomesticos import Electrodomesticos as el


def imprimir(li):
    for ele in li:
        print(ele.precioFinal())

if __name__ == "__main__":
    lista = []
    lista.append(Lavadora(precioBase=100,carga=300))
    lista.append(Lavadora(precioBase=200,carga=200, peso = 100, consumoEnergetico="A"))
    lista.append(Television(precioBase=120, color="NEGRO",peso=230))


    imprimir(lista)

    