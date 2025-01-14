from Clase import Vehiculo as ve

class Camion(ve):
    def __init__(self, ruedas, asientos, volante, carroceria, conductor, frenos, remolque, trailer, tara, mercancia):
        super().__init__(ruedas, asientos, volante, carroceria, conductor, frenos)
