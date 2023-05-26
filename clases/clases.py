class Perro():

    # constructor
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def habla(self):
        print(f"{self.nombre} dice Guau")


mi_perro = Perro('Rufus')
print(mi_perro.nombre)
mi_perro.habla()

# ? verificar si esa instancia pertenece a esa clase
print(isinstance(mi_perro, Perro))
