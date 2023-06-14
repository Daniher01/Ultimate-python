import json
from pathlib import Path

# #?  escribir json
# produdctos = [
#     {"id": 1, "name": "Surdboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]
# data = json.dumps(produdctos) # lo convierte a formato json
# Path("archivos/productos.json").write_text(data)

#? leer json
data = Path("archivos/productos.json").read_text(encoding="UTF-8")
productos = json.loads(data)
print(productos)

#? modificar json
productos[0]['name'] = 'nombre editado'
data = json.dumps(productos) # lo convierte a formato json
Path("archivos/productos.json").write_text(data)