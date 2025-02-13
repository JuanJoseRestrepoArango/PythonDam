from .Electrodomesticos import Electrodomesticos as el

class Lavadora(el):
    _CARGA_DEF = 5

    def __init__(self, precioBase=el._PRECIO_DEF, color=el._COLOR_DEF, consumoEnergetico=el._CONSUMO_ENE_DEF, peso=el._PESO_DEF, carga = _CARGA_DEF):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.carga = carga

    def __str__(self) -> str:
        return super().__str__() +f'carga = {self.carga}'
    
    def precioFinal(self):
        plus = super().precioFinal()
        if(self.carga > 30):
            return plus + 30
        return plus
        