""" 
poder restar dias 
"""

from datetime import datetime, timedelta

fecha1 = datetime(2023, 1,1) + timedelta(weeks=1) # si le quiero agregar, por ejemplo, 1 semana
fecha2 = datetime(2023,2,1)

delta = fecha2 - fecha1 # ? deiferencias de una fecha con respecto a la otra
print(delta) 
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())