import sqlite3

""" 
conn -> gestiona la conexion
cursor -> gestiona las consutlas
"""

conn = sqlite3.connect("sqlite/app.db")
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
# compromete/guarda los cambios
conn.commit() #! importante
conn.close()