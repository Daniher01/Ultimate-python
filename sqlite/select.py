import sqlite3

#? select-one
with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    print(cursor.fetchone())

#? select-all   
with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    print(cursor.fetchall()) 