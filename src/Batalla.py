import pickle
import os
import src.Elemento
import src.Monstruo
import src.JuegoExcepciones


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

    def actualizar_turno(self):
        self.turno = Turno((self.turno.value + 1) % 2)

    def mostrar_turno(self):
        print("\t****  Es el turno de [" + str(self.turno) + "] ****")
        print("\t**********************************************")

    def elegir_ataque(self, jugador):
        try:
            dict_opciones_ataque = dict()
            idx_op = 1
            print("\t\tElija el tipo de ataque que desea utilizar")
            for elem in jugador.elementos:
                opcion = "ESPECIAL tipo " + str(elem)
                dict_opciones_ataque[idx_op] = tuple(opcion elem)
                idx_op += 1

            if jugador.cant_esp_att < jugador.max_cant_esp_att:
                for elem in jugador.elementos:
                    #print("\t\t[" + str(idx_op) + "] ESPECIAL tipo " + str(elem))
                    dict_opciones_ataque[idx_op] = tuple("ESPECIAL tipo ", elem)
                    idx_op += 1

            dict_opciones_ataque[idx_op] = tuple("Guardar ", elem)
            idx_op += 1

            dict_opciones_ataque[idx_op] = tuple("ESPECIAL tipo ", elem)
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

    def resumen_ronda(self):
        print("\n\t\tResumen de la ronda...")
        for jugador in self.jugadores:
            print("\t" + str(jugador))

    def controlar_fin(self):
        for jugador in self.jugadores:
            if jugador.vida == 0:
                raise JuegoFinalizadoException

    def pelear(self, ataque_elegido, tipo_elemento_ataque):
        ataque_elegido = 0
        tipo_elemento_ataque = 0
        danio_total = 0
        calculo = ""
        restart = 0

        danio_total, danio_base, plus_ataque, plus_defensa = defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

        print("\n\t\tDanio calculado por Jugador " + str(defiende.id_jugador) + "")
        print("\t\t[Danio Total = Danio Base + Plus Ataque - Plus Defensa]")
        print("[ " + str(danio_total) + " = " + str(danio_base) + " + " + str(plus_ataque) + " - " + str(plus_defensa) + "]")
        print("\t\tPunto de vida: [" + str(defiende.vida) + "]")
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
