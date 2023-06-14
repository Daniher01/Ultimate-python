import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    usuarios = [
        (2, 'Chanchito feliz'),
        (3, 'Chanchito triste')
    ]
    cursor.executemany( #! se usa excecute many en lugar d execute
        "insert into usuario values(?, ?)",
        # se le pasa una tupla con los valores
        usuarios
    )