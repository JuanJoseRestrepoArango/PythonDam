from Clase import Vehiculo as ve

class Moto(ve):
    def __init__(self, asientos, volante, carroceria, conductor, frenos):
        super().__init__(2, asientos, volante, carroceria, conductor, frenos)
