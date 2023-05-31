class Perro:
    def __init__(self, nombre):
        self.nombre = nombre  # metodo con lógica de validacion

    # ? asigna ese metodo como el getter de la propiedad (en este caso self.__nombre)
    @property
    def nombre(self):
        print('pasando por getter')
        return self.__nombre

    # ? asigna este metodo como el setter de la propiedad (en este caso self.__nombre)
    @nombre.setter
    def nombre(self, nombre):
        print('pasando por setter')
        if nombre.strip():
            # valida que el nombre sea un string con datos
            self.nombre = nombre
        return

    """
    Ventajas de usar el decorador @property
    - los metodos quedan completamente privados y no se ven fuera de la clase
    """


perro = Perro('rufencio')
print(perro.nombre)
