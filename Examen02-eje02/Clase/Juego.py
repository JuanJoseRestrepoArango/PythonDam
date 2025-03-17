class Juego:
    def __init__(self,jugadores,revolver ):
        self.jugadores = jugadores
        self.revolver = revolver

    def finJuego(self):
        for i in range(0,len(self.jugadores)):
            if(self.jugadores[i].vivo == False):
               return True
            else:
                return False
            
    def ronda(self):
        for i in range(0,len(self.jugadores)):
            self.jugadores[i].dispararJugador(self.revolver)
            self.revolver.siguienteBala()