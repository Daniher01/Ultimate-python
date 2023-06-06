"""
Trata de cuando una clase hereda de varias clases, ejemplo, gato hereda de perro y de animal

#? ideal: la clases que se van a usar para herencia multiple, que sean lo mas pequeñas posibles y los metodos no se repitan entre si(que animal no tenga la clase comer si perro ya la tiene o viceversa)
"""


class Animal:
    def comer(self):
        print("Comiendo")


class Perro():
    def pasear(self):
        print("Paseando")


class Gato(Animal, Perro):
    def programar(self):
        print("Programando")
