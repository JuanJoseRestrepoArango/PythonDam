from .Electrodomesticos import Electrodomesticos as el

class Television(el):
    _RESOULUCION_DEF = 20
    _SINTONIZADOR_DEF = False

    def __init__(self, precioBase=el._PRECIO_DEF, color=el._COLOR_DEF, consumoEnergetico=el._CONSUMO_ENE_DEF, peso=el._PESO_DEF, resolucion = _RESOULUCION_DEF, sintonizador = _SINTONIZADOR_DEF):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.resolucion = resolucion
        self.sintonizador = sintonizador

    def precioFinal(self):
        plus = super().precioFinal()
        if self.resolucion > 40:
            plus = plus + plus*0.3
        
        if self.sintonizador:
            plus = plus + 50

        return plus
    
    def __str__(self):
        return super().__str__() + f'Resolucion = {self.resolucion} Sintonizador = {self.sintonizador}'