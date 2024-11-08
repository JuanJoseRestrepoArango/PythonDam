from datetime import date, datetime,timedelta
import locale


fecha = input('Dime la fecha (dd/mm/yyyy)')
fecha = datetime.strptime(fecha,'%d/%m/%Y')
incremento = timedelta(days = 1)
locale.setlocale(locale.LC_ALL,"es_ES")
nueva = date(fecha.year,fecha.month,1)
while(nueva.month == fecha.month):
    if(nueva.weekday() ==0):
       print(nueva)
    nueva = nueva+incremento
    
    
    


