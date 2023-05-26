class Perro():

    # constructor
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    """
    toma este metodo de habla y lo conviernte en un metodo propio de la clase
    hay que cambie self -> cls para hacer referencia a esa clase (en este caso la clase Perro)
    """
    @classmethod
    def habla(cls):
        print("Guau")

    # * crear un factory method
    # * crea una instancia de esa clase
    @classmethod
    def factory(cls):
        return cls('Rufencio')


"""
antes habia que instanciar la clase para poder usar ese metodo, ejemplo: mi_perro.habla()
ahora solo con la clase se puede usar ese metodo Perro.habla()
"""
Perro.habla()
perro1 = Perro('Rufus')
perro2 = Perro('perrito')
perro3 = Perro.factory()
print(perro3.nombre)
