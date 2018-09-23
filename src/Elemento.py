from enum import Enum


class TipoAtaque(Enum):
    NORMAL = 10
    ESPECIAL = 15


class Turno(Enum):
    Jugador1 = 0
    Jugador2 = 1


class Elemento(Enum):
    NONE = (0, "NADA")
    AIRE = (1, "AIRE")
    TIERRA = (2, "TIERRA")
    AGUA = (3, "AGUA")
    FUEGO = (4, "FUEGO")

    def __str__(self):
        return self.value[1]

    def tiene_plus_ataque(self, elem):
        # Quien tiene plus de ataque contra param
        # AGUA --> AIRE --> TIERRA --> FUEGO --> AGUA
        if elem == Elemento.AGUA:
            return Elemento.AIRE
        elif elem == Elemento.AIRE:
            return Elemento.TIERRA
        elif elem == Elemento.TIERRA:
            return Elemento.FUEGO
        if elem == Elemento.FUEGO:
            return Elemento.AGUA

    def tiene_plus_defensa(self, elem):
        # AGUA --> TIERRA --> AIRE --> FUEGO --> AGUA
        if elem == Elemento.AGUA:
            return Elemento.TIERRA
        elif elem == Elemento.TIERRA:
            return Elemento.AIRE
        if elem == Elemento.AIRE:
            return Elemento.FUEGO
        elif elem == Elemento.FUEGO:
            return Elemento.AGUA


if __name__ == '__main__':
    el = Elemento(Elemento.AGUA)
    print(el)
