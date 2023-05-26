"""
Podemos eliminar el primer elemento de una fila y correr todos los elementos un espacio
gracias a deque

las filas siguen el concepto FIFO (first in first out)
# ? un ejemplo podria ser una fila de espera para atencion en el banco
"""

from collections import deque

fila = deque([1, 2])
fila.append(3)
print(fila)
fila.popleft()  # elimina el primer elemento
print(fila)
