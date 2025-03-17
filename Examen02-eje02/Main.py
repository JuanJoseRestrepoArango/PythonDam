from Clase.Juego import Juego
from Clase.Jugador import Jugador
from Clase.Revolver import Revolver
import random
jugadores = []

for i in range(1,6):
    jugadores.append(Jugador(i,f'Jugador {i}',True))

j1 = Juego(jugadores,Revolver(random.randint(1,6),random.randint(1,6)))
print("Inicio del Juego")
cont = 1
while(j1.finJuego() != True):
    print(f'Ronda {cont}')
    print(j1.revolver.__str__())
    j1.ronda()
    
    cont+=1


print("Fin del Juego")

