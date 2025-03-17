class Revolver:
    def __init__(self,posActual,posBala) :
        self.posActual = posActual
        self.posBala = posBala

    def disparar(self):
        if(self.posActual == self.posBala):
            return True
        
    def siguienteBala(self):
        if self.posActual == 6:
            self.posActual = 0
        elif self.posActual < 6:
            self.posActual +=1

    def __str__(self) -> str:
        return f'posicion actual {self.posActual} posicion bala{self.posBala}'
    