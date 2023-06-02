""" 
Estos metodos magicos se usan para comprar objetos
- si 2 objetos son iguales,
- si un objeto es mayor o igual a otro
"""


class Coordenadas:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, __value: object) -> bool:
        """permite comparar 2 objetos que aunque no esten en el mismo lugar en memoria, tiene los mismos valores

        Args:
            __value (object): _description_

        Returns:
            bool: _description_
        """
        return self.lat == __value.lat and self.lon == __value.lon

    def __ne__(self, __value: object) -> bool:
        """permite comparar si un objeto no es igual a otro objeto (lo contrario a __eq__)

        Args:
            __value (object): _description_

        Returns:
            bool: _description_
        """
        return self.lat != __value.lat or self.lon != __value.lon

    def __lt__(self, otro):
        """comprar objetos si uno es mayor a otro

        Args:
            otro (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        """comprar objetos si uno es mayor o igual a otro

        Args:
            otro (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
# ? permite comparar si los objetos son los mismos
# ? es decir que si existen en el mismo lugar en memoria
print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)
