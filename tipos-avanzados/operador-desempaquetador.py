"""
desempaqueta una lista o tupla
"""
lista1 = [1, 2, 3, 4, 5]

lista2 = [5, 6]

combinada = ["hola", *lista1, "mundo", *lista2, "chancho"]

print(combinada)

"""
desempaquetando diccionario
"""

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}

print(nuevoPunto)
