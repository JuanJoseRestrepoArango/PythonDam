class Vehiculo:
    def __init__(self, ruedas, asientos, volante, carroceria, conductor, frenos):
        self.ruedas = ruedas
        self.asientos = asientos
        self.volante = volante
        self.carroceria = carroceria
        self.conductor = conductor
        self.frenos = frenos
    def _ver_ruedas(self):
        print(self.ruedas)
    def cambiar_conductor(self, conductor):
        self.conductor = conductor
    def ver_conductor(self):
        print(self.conductor)

    def mph_to_km(self, mph):
        print(1.6 *mph)


        
