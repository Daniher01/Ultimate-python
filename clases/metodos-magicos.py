"""
Metodos Magicos

- son metodos que se van a ejecutar cuando no los estemos llamando directamente
ejemplo -> el metodo __init__ (constructor)

# ? listado de metodos https://rszalski.github.io/magicmethods/
"""


class Perro:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    # ejemplo de metodo magico
    def __str__(self) -> str:
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro('rufencio', 10)
print(perro)
texto = str(perro)  # llama la funcion str
print(texto)
