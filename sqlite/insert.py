import sqlite3

""" 
usar (?) con tuplas es una forma de seguridad para prevenir el sql injection
"""


with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "insert into usuario values(?, ?)",
        # se le pasa una tupla con los valores
        (1,'Hola mundo'),
    )