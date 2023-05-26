"""
Se pueden modificar y filtrar elementos de una lista sin recorrerla manualmente

# ? nombres = [expresion for item in items if condicion] 
"""


usuarios = [
    ['Daniel', 4],
    ['Juan', 1],
    ['Johanna', 5]
]

# modificar
nombres = [usuario[0] for usuario in usuarios]
# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


"""
? MAP Y FILTER

- map(funcion para cada elemento de la lista, lista)

- filter(condicion, lista)
"""
nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(nombres)
print(menosUsarios)


"""
#? Se puede usar comprension de listas o map y filter
"""
