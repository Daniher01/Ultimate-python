""""
- Permite convertir los parametros de una funcion en iterables
- Una misma llamada a la funcion puede tener distintos numeros de argumentos
"""


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3, 4)
suma(10, 4)
suma(1, 2, 3, 4)
