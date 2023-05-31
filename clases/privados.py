class Perro():

    # constructor
    def __init__(self, nombre) -> None:
        # ? un atributo es privado cuando se le asigna __ antes del nombre, ejemplo __nombre
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau")

    # ? una opcion para poder leer el nombre del perro
    # * esto solo permite leer el nombre mas no modificarlo
    def get_nombre(self):
        return self.__nombre

    # ? si se necesita modificar el nombre del perro (de manera mas segura)
    def set_nombre(self, nombre):
        """
        si se desean hacer ciertas condiciones para permitir el cambio de nombre del perro
        se pueden hacer AQUI (lógica de negocio)
        ejemplo:
        - solo si el perro es adoptado
        - no se puede guardar un string vacio o algun numero negativo como nombre
        """
        self.__nombre = nombre

    # ? se puede crear también un metodo privado agregandole __ antes del nombre del método
    def __metodo_privado():
        print('este es un metodo privado')

    @classmethod
    def factory(cls):
        return cls('Rufencio')


perro1 = Perro.factory()
perro1.habla()
# va a dar error
# print(perro1.__nombre)
print(perro1.get_nombre())

# diccionario con todas las propiedades del objeto
print(perro1.__dict__)
print(perro1._Perro__nombre)  # ! no recomendado
