from datetime import datetime,timedelta

import locale

fecha = input("Ingrese una fecha (dd/mm/yyyy)? ")

fecha = datetime.strptime (fecha, "%d/%m/%Y")

fecha = fecha.replace(day = 1)
m = fecha.month
n = fecha.weekday()
inc = timedelta(days=1)
cadena =  "   "*n
print("L  M  M  J  V  S  D  ")
while(fecha.month == m):
    n = fecha.day    
    cadena  = cadena+f'{str(n):3}'
    if (fecha.weekday() == 6):
        print(cadena)
        cadena = ""
    fecha = fecha+inc
print(cadena)
fecha = fecha + timedelta(days = -1)
print("EL ULTIMO DIA DEL MES ES:")
print(fecha.strftime("%A %d de %B del %Y ").upper())
