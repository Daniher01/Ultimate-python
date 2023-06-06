""" 
La clase "Model" está apta para instanciar, pero el PROBLEMA es
que esta clase no deberia estar apta para instanciarse

Ahi entran las CLASES ABSTRACTAS
- No permite instanciar una clase abstracta
- Hay que definir todos los atributos de esa clase abstracta en la clase hija si se le pide
- Como tiene un metodo con @abstractclassmethod no necesita un constructor 
"""

from abc import ABC, abstractclassmethod


class Model(ABC):
    # la clase abstracta debe heredad de ABC

    @property  # lo convierte en una propiedad de solo lectura
    @abstractclassmethod  # hace que sea obligatorio declararlo en la clase hija
    def tabla(self):
        pass

    @abstractclassmethod
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    # hay que implementar el metodo de guardar
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
# model = Model() #! va a dar error porque es una clase absctracta
