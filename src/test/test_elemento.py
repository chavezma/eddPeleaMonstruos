import unittest
from src.Elemento import Elemento


class TestElemento(unittest.TestCase):

    def setUp(self):
        self.elemGenerico = Elemento(Elemento.NONE)

    def test_creaar_elemento_vacio(self):
        elemNinguno = Elemento(Elemento.NONE)
        self.assertEqual(elemNinguno.value[0], 0, "error al crear elemento VACIO")
        self.assertEqual(elemNinguno.value[1], "NADA", "error al crear elemento VACIO")

    def test_creaar_elemento_aire(self):
        elemAire = Elemento(Elemento.AIRE)
        self.assertEqual(elemAire.value[0], 1, "error al crear elemento AIRE")
        self.assertEqual(elemAire.value[1], "AIRE", "error al crear elemento AIRE")

    def test_creaar_elemento_tierra(self):
        elemTierra = Elemento(Elemento.TIERRA)
        self.assertEqual(elemTierra.value[0], 2, "error al crear elemento TIERRA")
        self.assertEqual(elemTierra.value[1], "TIERRA", "error al crear elemento TIERRA")

    def test_creaar_elemento_agua(self):
        elemAgua = Elemento(Elemento.AGUA)
        self.assertEqual(elemAgua.value[0], 3, "error al crear elemento AGUA")
        self.assertEqual(elemAgua.value[1], "AGUA", "error al crear elemento AGUA")

    def test_creaar_elemento_fuego(self):
        elemFuego = Elemento(Elemento.FUEGO)
        self.assertEqual(elemFuego.value[0], 4, "error al crear elemento FUEGO")
        self.assertEqual(elemFuego.value[1], "FUEGO", "error al crear elemento FUEGO")

    # Quien tiene plus de ataque contra cada elemento
    # AIRE --> TIERRA
    # TIERRA --> FUEGO
    # AGUA --> AIRE
    # FUEGO --> AGUA
    def test_tiene_plus_ataque_aire(self):
        elemAire = Elemento(Elemento.AIRE)
        self.assertEqual(self.elemGenerico.tiene_plus_ataque(elemAire), Elemento(Elemento.TIERRA), "error al validar plus ataque de AIRE")

    def test_tiene_plus_ataque_tierra(self):
        elemTierra = Elemento(Elemento.TIERRA)
        self.assertEqual(self.elemGenerico.tiene_plus_ataque(elemTierra), Elemento(Elemento.FUEGO), "error al validar plus ataque de TIERRA")

    def test_tiene_plus_ataque_agua(self):
        elemAgua = Elemento(Elemento.AGUA)
        self.assertEqual(self.elemGenerico.tiene_plus_ataque(elemAgua), Elemento(Elemento.AIRE), "error al validar plus ataque de AGUA")

    def test_tiene_plus_ataque_fuego(self):
        elemFuego = Elemento(Elemento.FUEGO)
        self.assertEqual(self.elemGenerico.tiene_plus_ataque(elemFuego), Elemento(Elemento.AGUA), "error al validar plus ataque de FUEGO")

    # Quien tiene plus de defensa contra cada elemento
    # AIRE --> FUEGO
    # TIERRA --> AIRE
    # AGUA --> TIERRA
    # FUEGO --> AGUA

    def test_tiene_plus_defensa_aire(self):
        elemAire = Elemento(Elemento.AIRE)
        self.assertEqual(self.elemGenerico.tiene_plus_defensa(elemAire), Elemento(Elemento.FUEGO), "error al validar plus defensa de AIRE")

    def test_tiene_plus_defensa_tierra(self):
        elemTierra = Elemento(Elemento.TIERRA)
        self.assertEqual(self.elemGenerico.tiene_plus_defensa(elemTierra), Elemento(Elemento.AIRE), "error al validar plus defensa de TIERRA")

    def test_tiene_plus_defensa_agua(self):
        elemAgua = Elemento(Elemento.AGUA)
        self.assertEqual(self.elemGenerico.tiene_plus_defensa(elemAgua), Elemento(Elemento.TIERRA), "error al validar plus defensa de AGUA")

    def test_tiene_plus_defensa_fuego(self):
        elemFuego = Elemento(Elemento.FUEGO)
        self.assertEqual(self.elemGenerico.tiene_plus_defensa(elemFuego), Elemento(Elemento.AGUA), "error al validar plus defensa de FUEGO")


if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
