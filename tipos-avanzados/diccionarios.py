"""
colecicon de datos agrupados por una llave y un valor
"""
punto = {"x": 25, "y": 50}

print(punto)
# acceder
print(punto["x"])
# agregar datos
punto["z"] = 45
print(punto)
# saber si un una key existe
if "lala" in punto:
    print('si existe lala ', punto["lala"])

# otra manera de acceder
print(punto.get("x"))
# segundo valor para mostrar si no existe la llave
print(punto.get("lala", 97))
# eliminar un valor
del punto["y"]
print(punto)

# recorrer un diccionario opcion 1
for valor in punto.items():
    print(valor)  # devuelve una tupla

# recorrer un diciconario opcion 2
for key, valor in punto.items():
    print(key, valor)

# ? ejemplo mas cotidiano
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Daniel"},
]

for usuario in usuarios:
    print(usuario["nombre"])
