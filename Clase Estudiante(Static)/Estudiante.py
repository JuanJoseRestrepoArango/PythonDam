class Estudiante:
    escuela = "EAFIT"
    def __init__(self, nombre , direccion) :
        self.nombre = nombre
        self.direccion = direccion
    def __str__(self) -> str:
        return f'{self.nombre} {self.direccion} {Estudiante.escuela} {self.escuela}'        