"""
la colas siguen el concepto LIFO (last in first out)

# ? un ejemplo podria ser la historial de navegación
"""
pila = []

pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo_elemento = pila.pop()  # elimina el ultimo elemento
print(ultimo_elemento)
print(pila)
print(pila[-1])  # ultimo elemento de la pila
# si ya no hay datos en la pila
if not pila:
    print('pila vacia')
