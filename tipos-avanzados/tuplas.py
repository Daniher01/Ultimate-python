"""
Las tuplas son como listas pero no se pueden modificar, ni agregar ni quitar elementos
    se pueden hacer todas la operaciones que con una lista excepto las que nos permitan modificarlas
"""
# una opcion de crear tuplas
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)


# otra opcion de crear tuplas
punto = tuple([1, 2])
print(punto)

# acceder
menosNumeros = punto[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

"""
? si quisieramos modificar una tupla (no ideas)
? habría que crea una lista donde se le pase esa tupla
? ejemplp list(tupla)
"""
