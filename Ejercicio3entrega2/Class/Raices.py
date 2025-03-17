import math
class Raices:
    def __init__(self,ca,cb,cc) :
        self.ca = ca
        self.cb = cb
        self.cc = cc

    def obtenerRaices(self):
        resultado = []
        resultado.append((-self.cb + math.sqrt(pow(self.cb,2)-4*self.ca*self.cc))/(2*self.ca))
        resultado.append((-self.cb - math.sqrt(pow(self.cb,2)-4*self.ca*self.cc))/(2*self.ca))
        return resultado
    def obtenerRaiz(self):
        return -self.cb/(2*self.ca)
    def getDiscriminante(self):
        return (pow(self.cb, 2)) -4*self.ca*self.cc
	
    def tieneRaices(self):
        if(self.getDiscriminante() >= 0):
            return True
        return False
    
    def tieneRaiz(self):
        if(self.getDiscriminante() == 0):
            return True
        return False
    
    def calcular(self, r1):
        if(r1.getDiscriminante() == 0):
            print(f' Raiz = {r1.obtenerRaiz()}')
        elif(r1.tieneRaices()):
            raices = r1.obtenerRaices()
            for i in raices:
                print(f'Raiz numero {raices.index(i) +1} = {i}')

        else:
            print("No tiene Raices")

    def __str__(self) -> str:
        return f' coeficiente a = {self.ca}  coeficiente b = {self.cb}  coeficiente c = {self.cc}'

    
    