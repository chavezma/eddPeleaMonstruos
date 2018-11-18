from src.Elemento import Elemento
from src.Elemento import Turno
from src.Elemento import TipoAtaque
import src.Monstruo


class Batalla:

    def __init__(self):
        self.jugadores = []
        self.turno = Turno(0)
        #self.jugador = 1
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

    def finalizado(self, defiende):
        if defiende.vida == 0:
            return True
        else:
            return False

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
        atacante = self.obtener_atacante()

        if ataque_elegido == TipoAtaque.ESPECIAL:
            atacante.cant_esp_att += 1

        self.calculo_danio = defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

        return "Continuar"
