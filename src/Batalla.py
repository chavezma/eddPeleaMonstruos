import pickle
import os
from Elemento import Turno
from Elemento import Elemento
from Elemento import tipo_ataque
from Monstruo import Monstruo
from JuegoExcepciones import JuegoMenuPrincipalException
from JuegoExcepciones import JuegoGuardadoException
from JuegoExcepciones import JuegoGuardarException


class Batalla:

    def __init__(self):
        self.jugadores = []
        self.turno = Turno.Jugador1
        self.jugador = 1

    def __str__(self):
        monstruos = ""
        for m in self.jugadores:
            monstruos += str(m) + "\n"
        monstruos += "\tBatalla Turno = [" + str(self.turno) + "]"
        return monstruos

    def mostrar_turno(self):
        print("\t****  Es el turno de [" + str(self.turno) + "] ****")
        print("\t**********************************************")

    def elegir_ataque(self, jugador):
        lista_op_validas = [1, 2, 3, 4, 5, 6]
        idxopelegida = 0
        op_ok = "NO"

        while idxopelegida not in  lista_op_validas:
            idx_op = 1
            try:
                print("\t\tElija el tipo de ataque que desea utilizar")
                for elem in jugador.elementos:
                    print("\t\t[" + str(idx_op) + "] NORMAL tipo " + str(elem))
                    idx_op += 1

                if jugador.cant_esp_att < jugador.max_cant_esp_att:
                    for elem in jugador.elementos:
                        print("\t\t[" + str(idx_op) + "] ESPECIAL tipo " + str(elem))
                        idx_op += 1

                print("\t\t[5] Guardar.")
                print("\t\t[6] Menu Principal.")

                idxopelegida = int(input("\t\tElegir opcion: "))

            except ValueError:
                raise ValueError("error al elegir ataque, restauro")

        if idxopelegida == 1:
            return tipo_ataque.NORMAL, jugador.elementos[0]
        elif idxopelegida == 2:
            return tipo_ataque.NORMAL, jugador.elementos[1]
        elif idxopelegida == 3:
            if jugador.cant_esp_att >= jugador.max_cant_esp_att:
                raise ValueError("error al elegir ataque, restauro")
            jugador.cant_esp_att = jugador.cant_esp_att + 1
            return tipo_ataque.ESPECIAL, jugador.elementos[0]
        elif idxopelegida == 4:
            if jugador.cant_esp_att >= jugador.max_cant_esp_att:
                raise ValueError("error al elegir ataque, restauro")
            jugador.cant_esp_att = jugador.cant_esp_att + 1
            return tipo_ataque.ESPECIAL, jugador.elementos[1]
        elif idxopelegida == 5:
            raise JuegoGuardarException
        elif idxopelegida == 6:
            raise JuegoMenuPrincipalException

    def pelear(self):
        ataque_elegido = 0
        tipo_elemento_ataque = 0
        danio_total = 0
        calculo = ""
        restart = 0

        if self.turno == Turno.Jugador1:
            ataca = self.jugadores[Turno.Jugador1.value]
            defiende = self.jugadores[Turno.Jugador2.value]
        else:
            ataca = self.jugadores[Turno.Jugador2.value]
            defiende = self.jugadores[Turno.Jugador1.value]

        self.mostrar_turno()

        try:
            ataque_elegido, tipo_elemento_ataque = self.elegir_ataque(ataca)
        except ValueError:
            print("\n\t\tLa opcion elegida no es valida.\n")
            input("\t\tPresionar una tecla para continuar...")
            return "continue"
        except JuegoGuardarException:
            return "guardar"
        except JuegoMenuPrincipalException:
            return "menu"

        danio_total, calculo = defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

        print("\n\t\tDanio calculado por Jugador " + str(defiende.id_jugador) + "")
        print("\t\t[Danio Total = Danio Base + Plus Ataque - Plus Defensa]")
        print("\t\t" + calculo)
        print("\t\tPunto de vida: [" + str(defiende.vida) + "]")
        input("")

        if self.turno == Turno.Jugador2:
            print("\n\t\tResumen de la ronda...")
            for jugador in self.jugadores:
                print("\t" + str(jugador))

        self.turno = Turno((self.turno.value + 1) % 2)

        for jugador in self.jugadores:
            if jugador.vida == 0:
                salir = "si"
                print("\n\t\tEl juego ha finalizado...")
                input("")

        input("\n\t\tpresioanr cualquier tecla para continuar...")
        return "continuar"


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
