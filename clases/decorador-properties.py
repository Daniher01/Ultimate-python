""" 
El decorador @property se utiliza para convertir un metodo en un atributo solo de lectura,
es decir, que no se puede modificar, un ejemplo es el metodo get() que solo se usa para obtener datos, no para modificarlos
"""


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre  # metodo con lógica de validacion -> setter
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
            self.__nombre = nombre
        return

    """
    Ventajas de usar el decorador @property
    - los metodos quedan completamente privados y no se ven fuera de la clase
    """


perro = Perro('rufencio')
print(perro.nombre)
