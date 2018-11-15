from src.Elemento import *


class Monstruo():

    # Un monstruo recibe el nombre y una lista de elementos
    def __init__(self, id, nombre, elementos):
        assert nombre, 'El nombre no puede ser vacio'
        self.nombre = nombre
        assert len(elementos) == 2, 'Debe tener dos elementos'
        self.elementos = elementos
        self.vida = 100
        self.max_cant_esp_att = 4
        self.cant_esp_att = 0
        self.id_jugador = id

    def __str__(self):
        printelem = "[" + str(self.elementos[0]) + ", " + str(self.elementos[1]) + "]"

        return "\tMonstruo = [" + str(self.nombre) + "] at_esp_usados [" + str(self.cant_esp_att) + "/" + str(self.max_cant_esp_att) + "] vida [" + str(self.vida) + "] - elementos " + printelem
        # return self.nombre + ";" + str(self.vida) + ";" + printelem

    def calcular_disminucion_danio(self, danio_base, t_elem_ataque):
        fortalezas = []
        plus_defensa = 0

        for mi_elem in self.elementos:
            fortalezas.append(Elemento(Elemento.NONE).tiene_plus_defensa(mi_elem))

        if t_elem_ataque in fortalezas:
            plus_defensa = danio_base * 0.2

        return plus_defensa

    def calcular_aumento_danio(self, danio_base, t_elem_ataque):
        debilidades = []
        plus_ataque = 0

        for mi_elem in self.elementos:
            debilidades.append(Elemento(Elemento.NONE).tiene_plus_ataque(mi_elem))

        if t_elem_ataque in debilidades:
            plus_ataque = danio_base*0.2

        return plus_ataque

    def actualizar_vida(self, danio):
        self.vida -= danio

        if self.vida < 0:
            self.vida = 0

    def recibir_ataque(self, t_ataque, t_elem_ataque):
        danio_total = 0
        danio_base = 10
        plus_ataque = 0
        plus_defensa = 0

        danio_base = t_ataque.value[0]

        plus_defensa = self.calcular_disminucion_danio(danio_base, t_elem_ataque)
        plus_ataque = self.calcular_aumento_danio(danio_base, t_elem_ataque)
        danio_total = danio_base + plus_ataque - plus_defensa

        self.actualizar_vida(danio_total)

        return [danio_total, danio_base, plus_ataque, plus_defensa]

    def ataques_posibles(self):
        dict_opciones_ataque = dict()
        idx_op = 1

        for elem in self.elementos:
            dict_opciones_ataque[idx_op] = Ataque(TipoAtaque.NORMAL, elem)
            idx_op += 1

        if self.cant_esp_att < self.max_cant_esp_att:
            for elem in self.elementos:
                dict_opciones_ataque[idx_op] = Ataque(TipoAtaque.ESPECIAL, elem)
                idx_op += 1

        return dict_opciones_ataque


if __name__ == '__main__':
    elementos = [Elemento.AIRE, Elemento.TIERRA]
    nombre = "Splinter"

    ataque = TipoAtaque.ESPECIAL
    t_at = Elemento.FUEGO

    m = Monstruo(1, nombre, elementos)

    print(m.ataques_posibles())

    m.recibir_ataque(ataque, t_at)

    print(m)