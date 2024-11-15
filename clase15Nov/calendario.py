from datetime import datetime,timedelta

import locale

fecha = input("Ingrese una fecha (dd/mm/yyyy)? ")

fecha = datetime.strptime (fecha, "%d/%m/%Y")

fecha = fecha.replace(day = 1)
m = fecha.month
n = fecha.weekday()
inc = timedelta(days=1)
cadena =  "   "*n
while(fecha.month == m):
    n = fecha.day    
    cadena  = cadena+f'{str(n):3}'
    if (fecha.weekday() == 6):
        print(cadena)
        cadena = ""
    fecha = fecha+inc
print(cadena)
        
