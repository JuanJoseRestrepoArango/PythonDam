class Electrodomesticos:
    _COLOR_DEF = "NEGRO"
    _CONSUMO_ENE_DEF= 'F'
    _PRECIO_DEF = 100
    _PESO_DEF = 5 #_ SE UTIIZA PARA ATRIBUTOS PROTEGIDOS
    __colores = ["blanco", "negro", "rojo","azul", "gris"]
    __consumo = {"A":100,"B":80, "C":60, "D":50, "E":30, "F":10}#__ se utiliza para privadas

    def __init__(self, precioBase = _PRECIO_DEF,color=_COLOR_DEF,consumoEnergetico = _CONSUMO_ENE_DEF, peso = _PESO_DEF):
        self.precioBase = precioBase
        self.color = self.__comprobarColor(color)
        self.consumoEnergetico = self.__comprobarConsumo(consumoEnergetico)
        self.peso = peso

    def __comprobarColor(self,color):
        if color in self.__colores : 
            return color
        return self._COLOR_DEF
    
    def __comprobarConsumo(self, consumo):
        consumo = consumo.upper()
        if consumo >= 'A' and consumo <= 'F':
            return consumo
        return self._CONSUMO_ENE_DEF
    
    def precioFinal(self):
        precio = self.__consumo[self.consumoEnergetico]
        if(self.peso >= 0 and self.peso <=19):
            precio += 10
        elif(self.peso >= 20 and self.peso <= 49):
            precio+=50
        elif(self.peso >= 50 and self.peso <= 79):
            precio+=80
        elif(self.peso > 80 ):
            precio+=100
        return precio

    def __str__(self) -> str:
        return f" PrecioBase {self.precioBase} Color = {self.color} ConsumoEnergetico = {self.consumoEnergetico} Peso = {self.peso}"
        


