"""  
como trabajar con numeros aleatorios

Casos de uso:
- se pueden generar ID unicos con el timestamp + caracteres/numeros dados por random
"""
import random
import string

lista = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista)

print(
    random.random(), # numero float aleatorio
    random.randint(1,10), # numero entero aletaroio entre 1 y 10
    lista, # cambia el orden de la lista aleatoriamente
    random.choice(lista), # trae un numero aleatorio de la lista
    random.choices(lista, k=3), # retorna 3 elementos de la lista
    "".join(random.choices("abcdefg.,123", k=5)), #trae 5 caracteres aletaroios
)

chars = string.ascii_letters # caracteres de la a-z y A-Z
digitos = string.digits # digitos del 1-9
seleccion = random.choices(chars+digitos, k=16)
print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
