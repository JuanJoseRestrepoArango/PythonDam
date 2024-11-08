from datetime import date,datetime,timedelta
import locale 
def restarDias(fecha):
    global undiamenos
    locale.setlocale(locale.LC_ALL,"es_ES")
    while(fecha.strftime('%A') !='viernes'):
            fecha = fecha+undiamenos
    return fecha

def ultimoViernes(fecha):
    global undiamenos
    for i in range(1,13,1):
        if(i==12):
            fecha = date(fecha.year+1,1,1)+undiamenos
        else:
            fecha = date(fecha.year,i+1,1)+undiamenos
          
        print(restarDias(fecha))


        
undiamenos = timedelta(days=-1)        


hoy=date.today()
print(hoy.year,0)
print ("{}:{}:{}".format(hoy.day,hoy.month,hoy.year))

ahora = datetime.now()
print ("{}:{}:{}:{}:{}:{}".format(ahora.day,ahora.month,ahora.year,ahora.hour,ahora.minute,ahora.second))

fecha = datetime(2024,12,20,22,30,30,0000)
print ("{}:{}:{}:{}:{}:{}".format(fecha.day,fecha.month,fecha.year,fecha.hour,fecha.minute,fecha.second))

format = fecha.strftime('Dia : %d, Mes : %m, Año : %Y, Hora: %H, Minutos : %M, Segundos: %S')
print(format)

print(fecha.weekday())

locale.setlocale(locale.LC_ALL,"es_ES")
print(fecha.strftime('%A %B %Y'))

fecha = fecha+timedelta(days=4)
print(fecha.strftime('%A %B %Y'))
ultimoViernes(fecha)