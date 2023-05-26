"""Calculadora """

# ? mi solucion

# print("""Bienvenidos a la Calculadora \nPara terminar, escriba: salir \nLas operacioens son suma, resta, multi y div""")

# numero1 = int(input('Ingrese un numero: '))

# while True:

#     operacion = input('Ingrese operacion ').strip().lower()
#     numero2 = input('Ingrese otro numero: ')

#     if operacion == 'salir' or numero2 == 'salir':
#         break

#     numero2 = int(numero2)
#     if operacion == 'suma':
#         resultado = numero1 + numero2
#     elif operacion == 'resta':
#         resultado = numero1 - numero2
#     elif operacion == 'multi':
#         resultado = numero1 * numero2
#     elif operacion == 'div':
#         resultado = numero1 / numero2

#     print(f'el resultado es {resultado}')
#     numero1 = numero2


# ? --------------- SOLUCION SUGERIDA
print("""Bienvenidos a la Calculadora \nPara terminar, escriba: salir \nLas operacioens son suma, resta, multi y div""")

resultado = ""
while True:
    if not resultado:
        resultado = input('Ingrese numero: ')
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)

    op = input('Ingresa operacion: ')
    if op.lower() == 'salir':
        break
    n2 = input('Ingrese siguiente numero: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multi':
        resultado *= n2
    elif op.lower() == 'div':
        resultado /= n2
    else:
        print('Operacion no valida')
        break
    print(f"El resultado es {resultado}")
