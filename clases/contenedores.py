""" 
Es una manera de almacenar objetos dentro de objetos
En este caso almacenar productos dentro de categorias
"""


class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos) -> None:
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 750)

deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
