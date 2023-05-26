# pylint: disable=missing-docstring

def eliminar_espacios(texto):
    lista_letras = []
    for caracter in texto:
        if caracter != " ":
            lista_letras.append(caracter)
    return lista_letras


def reverse_palabra(palabra):
    nueva_palabra = []
    for letra in palabra:
        nueva_palabra.insert(0, letra)
    return nueva_palabra


def es_palindromo(palindromo):
    palabra_sin_espacios = eliminar_espacios(palindromo.lower())
    palabra_volteada = reverse_palabra(palabra_sin_espacios)

    return palabra_sin_espacios == palabra_volteada


print('Abba', es_palindromo('Abba'))
print('Daniel', es_palindromo('Daniel'))
