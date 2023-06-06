""" 
Permite tener varios objetos de diferentes tipos pero que sean
manipulados de manera similar a través de una interfaz comun

- necesitan ser heredadas de la misma clase o interfaz
- al ser heredadas de la misma interfaz, se pueden tratar de manera similar porque van a tener los mismo metodos
-- en este caso el metodo "guardar_lo_necesario()" permite aplicar el mismo comportamiento a 2 instancias distintas (usuario, sesion)
"""

from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print(f"guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("guardando en archivo")


def guardar_lo_necesario(entidad):
    entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar_lo_necesario(usuario)
guardar_lo_necesario(sesion)
