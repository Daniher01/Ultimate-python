""" 
traduccion: ANULACIÓN DE METODO

trata de cuando obtenemos un metodo de una clase que hemos heredado y queremos modificarla cambiando su funcionalidad (solo en esa instancia)

super().metodo() permite tener todas las propiedades de ese metodo

"""

# ? CLASE PADRE


class Ave:

    def __init__(self) -> None:
        self.volador = "valador"

    def vuela(self):
        print("Vuela ave")


# ? CLASE HIJO o subclase
class Pato(Ave):
    def __init__(self) -> None:
        super().__init__()
        self.nada = "nadador"

    def vuela(self):
        super().vuela()
        print("vuela pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
