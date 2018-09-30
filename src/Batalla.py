from Elemento import Elemento
from Elemento import Turno
import Monstruo
import JuegoExcepciones


class Batalla:

    def __init__(self):
        self.jugadores = []
        self.turno = Turno(0)
        self.jugador = 1
        self.ronda = 0
        # Variables para el calculo del ultimo danio realizado --> danio_total, danio_base, plus_ataque, plus_defensa
        self.calculo_danio = [0, 0, 0, 0]

    def __str__(self):
        monstruos = ""
        for m in self.jugadores:
            monstruos += str(m) + "\n"
        monstruos += "\tUltimo Turno = [" + str(self.turno) + "]\n"
        monstruos += "\tRondas jugadas = [" + str(self.ronda) + "]"
        return monstruos

    def actualizar_turno(self):
        self.turno = Turno((self.turno.value + 1) % 2)

    def controlar_fin(self):
        defiende = self.obtener_defensor()
        if defiende.vida == 0:
            raise JuegoFinalizadoException

    def obtener_atacante(self):
        return self.jugadores[self.turno.value]

    def obtener_defensor(self):
        turno_def = Turno((self.turno.value + 1) % 2)
        return self.jugadores[turno_def.value]

    def pelear(self, ataque_elegido, tipo_elemento_ataque):
        danio_total = 0
        calculo = ""
        restart = 0

        defiende = self.obtener_defensor()

        self.calculo_danio = defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

        return "Continuar"


if __name__ == '__main__':
    b = Batalla()
    b2 = Batalla()
    elementos1 = [Elemento.AIRE, Elemento.TIERRA]
    nombre1 = "suri"

    elementos2 = [Elemento.AIRE, Elemento.AGUA]
    nombre2 = "pini"

    m1 = Monstruo(1, nombre1, elementos1)
    m2 = Monstruo(2, nombre2, elementos2)

    m1.vida = 80
    m2.vida = 70

    b.jugadores.append(m1)
    b.jugadores.append(m2)

    b.turno = Turno.Jugador1

    #with open('.//savedgames//data.save', 'wb') as output:
    #    pickle.dump(b, output, pickle.HIGHEST_PROTOCOL)

    #with open('.//savedgames//data.save', 'rb') as load:
    #    b2 = pickle.load(load)
    #    print(b2)
