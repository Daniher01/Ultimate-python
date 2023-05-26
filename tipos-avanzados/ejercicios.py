from pprint import pprint  # ? permite ver mejos los datos en consola
# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes
PALABRA = ' daniel hernandez '
lista_palabra = []
for letra in PALABRA:
    if letra != " ":
        lista_palabra.append(letra)
# print(lista_palabra)

# 2. contar en un diccionario cuanto se repiten los caracteres de un string
diccionario_palabra = {}
for char in lista_palabra:
    if char in diccionario_palabra:
        diccionario_palabra[char] += 1
    else:
        diccionario_palabra[char] = 1

pprint(diccionario_palabra, width=1)

# 3. ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas

# 4. ordenar el listado de tuplas por las del mayor valor
lista_ordenada = sorted(
    diccionario_palabra.items(), key=lambda x: x[1], reverse=True)
print(lista_ordenada)

# 5. mensaje con los caracteres que mas se repiten
print('los caracteres que mas se repiten son: ')
maximo = lista_ordenada[0][1]
respuesta = {}
for tupla in lista_ordenada:
    if maximo > tupla[1]:
        break
    # respuesta[tupla[0]] = tupla[1]
    mensaje = f"- {tupla[0]} con  {tupla[1]} repeticiones"
    print(mensaje)
