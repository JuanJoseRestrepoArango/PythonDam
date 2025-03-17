import numpy as np;
from ClaseAbstracta.Bebida import Bebida

class Almacen:
    def __init__(self,filas = 5,columnas = 5) :
        self.estanterias = np.zeros([filas,columnas], dtype= Bebida)

    def setEstanteria(self):
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                self.estanterias[i][j] = Bebida()


    def MostrarInformacion(self):
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                print(f"{self.estanterias[i][j]} ", end="")
            print()

    def CalcularPrecioBebidas(self):
        cont = 0
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                cont += self.estanterias[i][j].getPrecio()
        return cont
    
    def CalcularPrecioMarcaBebidas(self,marca):
        cont = 0
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                if(self.estanterias[i][j].getMarca() == marca):
                    cont += self.estanterias[i][j].getPrecio()
        return cont
    
    def CalcularPrecioEstanteria(self,estanteria):
        cont = 0
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                if (j == estanteria):
                    cont += self.estanterias[i][j].getPrecio()
        return cont
    
    def AgregarProducto(self,bebida):
        cont = 0
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                if(self.estanterias[i][j].getIdentificador() == 0 and self.estanterias[i][j].getIdentificador() != bebida.getIdentificador() and cont == 0):
                    self.estanterias[i][j] = bebida
                    cont +=1
                    

    def EliminarProducto(self,identificador):
        for i in range(0,len(self.estanterias)):
            for j in range(0,len(self.estanterias[i])):
                if(self.estanterias[i][j].getIdentificador() == identificador):
                    self.estanterias[i][j] = Bebida()

    


