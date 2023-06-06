""" 
Como extender tipos/clases nativas

en este ejemplo se pueden implementar clases con base a tipos nativos, como una lista y 
asi poder agregarles metodos propios para usarlas (en este caso) con una lista
"""


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista()
lista.append(4)
lista.prepend((0))
print(lista)
