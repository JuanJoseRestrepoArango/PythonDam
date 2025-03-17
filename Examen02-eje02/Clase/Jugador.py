class Jugador:
    def __init__(self,id,nombre ,vivo) :
        self.id = id
        self.nombre = nombre
        self.vivo = vivo


    def dispararJugador(self,revolver):
        if(revolver.disparar()):
            self.vivo = False
    
