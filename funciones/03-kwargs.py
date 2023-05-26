"""
kwargs -> key works arguments

Igual que los xargs pero al llamar a la funcion hay que especificarle el nombre del parametro
"""


def get_products(**datos):
    print(datos["id"])


get_products(id="23", name="Iphone", desc="Esto es un iphone")
