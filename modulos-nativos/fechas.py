# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2023,1,1) #? Y,m,d

ahora = datetime.now() # fecha actual
print(ahora)

# ? crear fechas a partir de strings
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr, type(fechaStr))

# ? crear un string a partir de una fecha
nuevo_formato_fecha = fecha.strftime("%Y.%m.%d")
print(nuevo_formato_fecha, type(nuevo_formato_fecha))

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)