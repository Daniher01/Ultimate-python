import sqlite3

""" 
gestionar consultas sin tener que estar cerrando siempre la conexion
"""

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor() # crea cursor
    # crea la consulta
    cursor.execute(
        """ 
        CREATE TABLE if not exists usuario(
            id INTEGER primary key,
            nombre VARCHAR(50)
        )
        """
    )
# no necesita ni commit() ni close()