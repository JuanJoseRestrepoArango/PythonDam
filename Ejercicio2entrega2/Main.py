from Class.Serie import Serie
from Class.VideoJuego import VideoJuego

countJuegos = 0
countSeries = 0

Juegos = []
Series = []

Juegos.append(VideoJuego("FIFA",20,"futbol","EA"))
Juegos.append(VideoJuego("GTA",50,"accion","Rockstar"))
Juegos.append(VideoJuego("LOL",100,"rol de accion","Riot Games"))
Juegos.append(VideoJuego("call of duty",20,"accion","Infinity Ward"))
Juegos.append(VideoJuego("Black Ops",20,"accion","Infinity Ward"))

Series.append(Serie("one piece",25,"anime","oda"))
Series.append(Serie("Naruto",10,"anime","kishimoto"))
Series.append(Serie("super campeones",15,"anime","takahashi"))
Series.append(Serie("my Hero academia",7,"anime","Horikoshi"))
Series.append(Serie("Black Ops",20,"accion","Infinity Ward"))

Series[2].entregar()
Series[0].entregar()
Juegos[2].entregar()
Juegos[0].entregar()

maxVideo = Juegos[0]
maxSerie = Series[0]

for i in Juegos:
    if(i.isEntregado()):
        countJuegos = countJuegos + 1
    maxVideo = maxVideo.compareTo(i)

for i in Series:
    if(i.isEntregado()):
        countSeries += 1
    maxSerie = maxSerie.compareTo(i)

print(f'Juegos entregados {countJuegos},  Series entregadas {countSeries}')
print(maxSerie)
print(maxVideo)

