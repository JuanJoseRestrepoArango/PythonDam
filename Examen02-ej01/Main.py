from Clase.Almacen import Almacen
from Clase.Azucarada import Azucarada
from Clase.Agua import Agua
import random

def definirBebida(identificador):
    op = int(input("Ingrese el tipo de bebida a agregar 1 para agua 2 para Bebida Azucarada "))
    cantidadLitros = int(input("Ingrese la cantidad de Litros "))
    precio = int(input("Ingrese el precio "))
    marca = input("Ingrese la marca ")
    if(op == 2):
        porAzucares = int(input("Ingrese el porcentaje de azucares "))
        promocion = int(input("Tiene promocion?1 para si 2 para no "))
        if(promocion == 1):
            bebida = Azucarada(identificador,cantidadLitros,precio,marca,porAzucares,True)
            bebida.VerificarPromocion()
        else:
            bebida = Azucarada(identificador,cantidadLitros,precio,marca,porAzucares,False)
    else:
        origen = input("Ingrese el origen ")
        bebida = Agua(identificador,cantidadLitros,precio,marca,origen)
    return bebida
        


        

if __name__ == "__main__":
    bebidasAzucaradas = ["Fanta","CocaCola","Sprite","Aquarium"]
    agua = ["Aguamanantial","AguaNormal"]
    origen = ["Manantial","rio","Pozo"]
    salir = "no"
    a1 = Almacen(5,5)
    a1.setEstanteria()
    cont = 1
    while(salir == "no"):
        a1.MostrarInformacion()
        agregar = int(input("Desea agregar una bebida? 1 para si 2 para no "))
        if(agregar == 1):
            a1.AgregarProducto(definirBebida(cont))
        a1.MostrarInformacion()
        print(f'Precio Total de Bebidas :{a1.CalcularPrecioBebidas()} ')
        marca = input("Ingrese la marca a analizar")
        print(f'Precio Total de Bebidas de CocaCola :{a1.CalcularPrecioMarcaBebidas(marca)} ')
        estanteria = int(input("Ingrese la estanteria a analizar"))
        print(f'Precio Total de Estanteria 1 :{a1.CalcularPrecioEstanteria(estanteria)} ')
        eliminar = int(input("Desea eliminar una bebida? 1 para si 2 para no "))
        if(agregar == 1):
            iden = int(input("Ingrese el identificador de la bebida a eliminar"))
            a1.EliminarProducto(iden)
       
        print()
        a1.MostrarInformacion()
        salir = input("Desea Salir?")
       