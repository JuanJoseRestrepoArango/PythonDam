import pytz
from datetime import datetime
import locale


for c,v in enumerate(pytz.all_timezones):
    dt = datetime.now(pytz.timezone(v))
    print(c,v,dt.strftime("%A %d de %B del %Y - %H:%M"))

locale.setlocale(locale.LC_ALL,"es_ES")
dt = datetime.now(pytz.timezone("Europe/Madrid"))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

dt = datetime.now(pytz.timezone("America/Bogota"))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))
