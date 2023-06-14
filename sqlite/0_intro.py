"""  
- Se usa para gestionar bases de datos pequeñas
- No es recomentable usar en producción
- Al conectarse a una bd de sqlite, SIEMPRE hay que cerrarla, sino, no se va a poder escribir en la bd
"""

import sqlite3

conn = sqlite3.connect("sqlite/app.db")
conn.close()