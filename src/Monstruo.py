from Elemento import Elemento
from Elemento import tipo_ataque
from Elemento import Turno

class Monstruo:

    # Un monstruo recibe el nombre y una lista de elementos
    def __init__(self, id, nombre, elementos):
        self.nombre = nombre
        self.elementos = elementos
        self.vida = 100
        self.max_cant_esp_att = 4
        self.cant_esp_att = 0
        self.id_jugador = id

    def __repr__(self):
        printelem = "["
        for x in self.elementos:
            printelem += str(x) + ","
        printelem += "]"

        return "\tMonstruo = [" + self.nombre + "] vida [" + str(self.vida) + "] - elementos " + printelem
        # return self.nombre + ";" + str(self.vida) + ";" + printelem

    def recibir_ataque(self, t_ataque, t_elem_ataque):
        fortalezas = []
        debilidades = []

        danio_total = 0
        danio_base = 10
        plus_ataque = 0
        plus_defensa = 0

        #print("\n\t recibi tipo ataque " + str(t_ataque))
        #print("\n\t recibi tipo elem ataque " + str(t_elem_ataque))

        if t_ataque == tipo_ataque.NORMAL:
            danio_base = 10
        elif t_ataque == tipo_ataque.ESPECIAL:
            danio_base = 15
            for mi_elem in self.elementos:
                debilidades.append( Elemento(1).tiene_plus_ataque(mi_elem) )

            #print(debilidades)
            if t_elem_ataque in debilidades:
                plus_ataque = danio_base*0.2

            for mi_elem in self.elementos:
                fortalezas.append( Elemento(1).tiene_plus_defensa(mi_elem) )

            #print(fortalezas)
            if t_elem_ataque in fortalezas:
                plus_defensa = danio_base*0.2

        danio_total = danio_base + plus_ataque - plus_defensa

        self.vida -= danio_total

        if self.vida < 0:
            self.vida = 0

        return danio_total, str("[ " + str(danio_total) + " = " + str(danio_base) + " + " + str(plus_ataque) + " - " + str(plus_defensa) + "]")


if __name__ == '__main__':
    elementos = [Elemento.AIRE, Elemento.TIERRA]
    nombre = "suri"

    ataque = tipo_ataque.ESPECIAL
    t_at = Elemento.FUEGO

    m = Monstruo(nombre, elementos)

    m.recibir_ataque(ataque, t_at)

    print(m)