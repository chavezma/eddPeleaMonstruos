import unittest
from src.Monstruo import Monstruo
from src.Elemento import Elemento
from src.Elemento import TipoAtaque


class TestMonstruo(unittest.TestCase):

    def setUp(self):
        self.myMonstruo = Monstruo(1, "Prueba", [Elemento.FUEGO, Elemento.AGUA])

    def test_validar_parametos_mostruo(self):
        self.assertEqual(100, self.myMonstruo.vida)
        self.assertEqual(4, self.myMonstruo.max_cant_esp_att)
        self.assertEqual(0, self.myMonstruo.cant_esp_att)
        self.assertEqual("Prueba", self.myMonstruo.nombre)

        self.assertEqual(self.myMonstruo.elementos[0].value[0], 4, "error al crear elemento FUEGO")
        self.assertEqual(self.myMonstruo.elementos[0].value[1], "FUEGO", "error al crear elemento FUEGO")

        self.assertEqual(self.myMonstruo.elementos[1].value[0], 3, "error al crear elemento AGUA")
        self.assertEqual(self.myMonstruo.elementos[1].value[1], "AGUA", "error al crear elemento AGUA")

    # Tengo plus de defensa contra:
    # por ser FUEGO tiene plus contra AGUA
    # por ser AGUA tiene plus contra TIERRA
    def test_calcular_disminucion_danio_normal(self):
        danio_base = TipoAtaque.NORMAL.value
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.AGUA)), 2, "error al validar daño normal contra AGUA")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.TIERRA)), 2, "error al validar daño normal contra TIERRA")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.AIRE)), 0, "error al validar daño normal contra AIRE")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.FUEGO)), 0, "error al validar daño normal contra FUEGO")

    def test_calcular_disminucion_danio_especial(self):
        danio_base = TipoAtaque.ESPECIAL.value
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.AGUA)), 3, "error al validar daño especial contra AGUA")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.TIERRA)), 3, "error al validar daño especial contra TIERRA")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.AIRE)), 0, "error al validar daño especial contra AIRE")
        self.assertEqual(self.myMonstruo.calcular_disminucion_danio(danio_base, Elemento(Elemento.FUEGO)), 0, "error al validar daño especial contra FUEGO")

    # Tienen plus de ataque contra mi
    # por ser FUEGO soy debil contra AGUA
    # por ser AGUA soy debil contra AIRE
    def test_calcular_auemnto_danio_normal(self):
        danio_base = 10
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.AGUA)), 2, "error al validar daño contra AGUA")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.TIERRA)), 0, "error al validar daño contra TIERRA")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.AIRE)), 2, "error al validar daño contra AIRE")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.FUEGO)), 0, "error al validar daño contra FUEGO")

    def test_calcular_aumento_danio_especial(self):
        danio_base = 15
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.AGUA)), 3, "error al validar daño contra AGUA")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.TIERRA)), 0, "error al validar daño contra TIERRA")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.AIRE)), 3, "error al validar daño contra AIRE")
        self.assertEqual(self.myMonstruo.calcular_aumento_danio(danio_base, Elemento(Elemento.FUEGO)), 0, "error al validar daño contra FUEGO")

    def test_actulizar_vida(self):
        danio1 = 10
        danio2 = 40
        danio3 = 80
        danio4 = 110

        self.myMonstruo.vida = 100
        self.myMonstruo.actulizar_vida(danio1)
        self.assertEqual(self.myMonstruo.vida, 90, "error al actualizar vida tras danio1")

        self.myMonstruo.vida = 100
        self.myMonstruo.actulizar_vida(danio2)
        self.assertEqual(self.myMonstruo.vida, 60, "error al actualizar vida tras danio")

        self.myMonstruo.vida = 100
        self.myMonstruo.actulizar_vida(danio3)
        self.assertEqual(self.myMonstruo.vida, 20, "error al actualizar vida tras danio3")

        self.myMonstruo.vida = 100
        self.myMonstruo.actulizar_vida(danio4)
        self.assertEqual(self.myMonstruo.vida, 0, "error al actualizar vida tras danio4")

    # Tienen plus de ataque contra mi      # Tienen plus de ataque contra mi
    # por ser FUEGO soy debil contra AGUA  # por ser FUEGO soy debil contra AGUA
    # por ser AGUA soy debil contra AIRE   # por ser AGUA soy debil contra AIRE
    def test_recibir_danio_normal_agua(self):
        t_at = TipoAtaque.NORMAL
        t_elem_at = Elemento.AGUA

        danio_total
        danio_base
        plus_ataque
        plus_defensa

        self.myMonstruo.recibir_ataque(t_at, t_elem_at)


if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
