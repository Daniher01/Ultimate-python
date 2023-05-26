"""
Coleccion de datos que no se puede repetir y que tampoco está ordenada
"""
primer = {1, 1, 2, 4, 3, 5, 5}
segundo = [3, 4, 5]
segundo = set(segundo)
# primer.add(6)
# primer.remove(1)
# print(primer)

# une los sets y elimina los repetidos #? | <- se conoce como "union"
print(primer | segundo)

# muestra solo los numeros que estan en ambos sets #? & <- intersecion
print(primer & segundo)

# muestra solo los numeros que NO estan en ambos sets #? - <- diferencia
print(primer - segundo)

# elimina todos los duplicados y muestra los no repetidos
# (parecido a el de diferencia) #? ^ <- diferencia simetrica
print(primer ^ segundo)

# ? accediento a un elemnto de un set
if 5 in segundo:
    print("hola mundo")

# no se puede
# segundo[0]
