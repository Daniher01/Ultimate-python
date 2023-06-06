"""
Trata de cuando una clase hereda de otra, por ejemplo, la clase perro hereda de la clase animal
"""


class Animal:
    def comer(self):
        print("Comiendo")


# se le pasa por parametro la clase de la cual hereda
class Perro(Animal):
    def pasear(self):
        print("Paseando")


class Gato(Animal):
    def programar(self):
        print("Programando")


rufus = Perro()
rufus.comer()
rufus.pasear()
obi = Gato()
obi.comer()
obi.programar()
