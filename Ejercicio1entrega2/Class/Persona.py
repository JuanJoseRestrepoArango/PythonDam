import random
class Persona:
    GENERO = 'H'
    ENFORMA = -1
    BAJOPESOIDEAL = 0
    SOBREPESO = 1

    def __init__(self, nombre = "", edad = 0 , sexo = GENERO, peso = 0, altura = 0.0) :
        self.__nombre = nombre
        self.__edad = edad
        self.__DNINIE = self.generarDNINIE()
        self.__sexo = self.comprobarSexo(sexo)
        self.__peso = peso
        self.__altura = altura


    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad
    
    def getSexo(self):
        return self.__sexo

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura
    def getDNINIE(self):
        return self.__DNINIE

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad
    
    def setSexo(self, sexo):
        self.__sexo = self.comprobarSexo(sexo)

    def setPeso(self, peso):
        self.__peso = peso

    def setAltura(self, altura):
        self.__altura = altura

    def esMayorDeEdad(self):
        if(self.getEdad() <18 ):
            return False
        return True

    def comprobarSexo(self,sexo):
        if(sexo == 'H' or sexo == 'M'):
            return sexo
        return self.GENERO
    
    def comprobarSobrePeso(self):
        calculo = self.getPeso()/pow(self.getAltura(),2)
        if(calculo<20):
            return self.ENFORMA
        elif(calculo>=20 and calculo <=25):
            return self.BAJOPESOIDEAL
        else:
            return self.SOBREPESO
        

    def generarDNINIE(self):
        cadena = ""
        Lnie = "XYZ"
        letra = "TRWAGMYFPDXBNJZSQVHLCKE"

        DNIoNIE = random.randint(1,2)

        if(DNIoNIE == 1):

            cadena = self.generar(8)
            numero = int(cadena)
            resto = numero % 23
            cadena = cadena + letra[resto]
            return cadena
        else:
            cadena = ""
            ra = random.randint(0,2)
            l = Lnie[ra]
            ind = Lnie.index(l)
            cadena = str(ind)+self.generar(7)
            numero = int(cadena)
            resto = numero %23
            cadena = l + cadena[1:] + letra[resto]

            return cadena


    
    def generar(self,n):
        cadena = ""
        for i in range(1,n,1):
            cadena = cadena + str(random.randint(0,9))
        return cadena
    
    def __str__(self) -> str:
        return f'nombre = {self.getNombre()} edad = {self.getEdad()} DNINIE = {self.getDNINIE()} sexo = {self.getSexo()} peso = {self.getPeso()} altura = {self.getAltura()}'
    
