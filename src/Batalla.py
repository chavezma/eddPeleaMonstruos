from Elemento import Turno
from Elemento import Elemento
from Elemento import tipo_ataque
from Monstruo import Monstruo
# Variables para iniciar-restaurar una batalla.

# Monstruo 1 [nombre, vida, elementos, cantAtaquesEsp, turno] 
# Monstruo 2 [nombre, vida, elementos, cantAtaquesEsp, turno]


class Battle:
    def __init__(self):
        self.jugadores = []
        self.turno = Turno.Jugador1
        self.jugador = 1

    def print_elementos(self, nro_elemento):
        if nro_elemento == 1:
            elem = "primer"
        else:
            elem = "segundo"

        print("Elija su " + elem + " elemento")
        print("[1] AIRE.")
        print("[2] TIERRA.")
        print("[3] AGUA.")
        print("[4] FUEGO.")

    def __repr__(self):
        return "Batalla Turno = [" + str(self.turno) + "]"

    def mostrar_turno(self):
        print("****  Es el turno de [" + str(self.turno) + "] ****")
        print("**********************************************")

    def crear_monstruo(self):
        elemento = []
        nombre = ""
        ups = Elemento(1)

        nombre = str(input("Ingrese su nombre:"))

        for idx_elemento in range(1, 3):
            self.print_elementos(idx_elemento)
            choose = int(input("Opcion:"))
            print("Eleccion realizada [" + str(choose) + "].")
            input("presionar algo....")
            elemento.append(Elemento(choose))

        return Monstruo(nombre, elemento)

    def config_jugadores(self, mostrar_titulo):
        idx_jugador = 0

        for idx_jugador in range(1, 3):
            mostrar_titulo()
            print("\n")
            print("****  Cargando informacion del jugador " + str(idx_jugador) + " ****")
            self.jugadores.append(self.crear_monstruo())

        for jugador in self.jugadores:
            print(jugador)

        input("...")

    def elegir_ataque(self, jugador):

        lista_op_validas = [1, 2, 3, 4, 5, 6]
        idxopelegida = 0
        op_ok = "NO"

        while op_ok == "NO":
            idx_op = 1
            print("Elija el tipo de ataque que desea utilizar")
            for elem in jugador.elementos:
                print("[" + str(idx_op) + "] NORMAL tipo " + str(elem))
                idx_op += 1

            if jugador.cant_esp_att < 4:
                for elem in jugador.elementos:
                    print("[" + str(idx_op) + "] NORMAL tipo " + str(elem))
                    idx_op += 1

            print("[5] Guardar.")
            print("[6] Salir.")

            idxopelegida = int(input("Elegir opcion: "))

            if idxopelegida in lista_op_validas:
                op_ok = "SI"

        if idxopelegida == 1:
            return tipo_ataque.NORMAL, jugador.elementos[0]
        elif idxopelegida == 2:
            return tipo_ataque.NORMAL, jugador.elementos[1]
        elif idxopelegida == 3:
            return tipo_ataque.ESPECIAL, jugador.elementos[0]
        elif idxopelegida == 4:
            return tipo_ataque.ESPECIAL, jugador.elementos[1]


    def comenzarpelea(self):
        ataque_elegido = 0
        tipo_elemento_ataque = 0

        salir = "no"
        while salir == "no":

            if self.turno == Turno.Jugador1:
                ataca = self.jugadores[Turno.Jugador1.value]
                defiende = self.jugadores[Turno.Jugador2.value]
            else:
                ataca = self.jugadores[Turno.Jugador2.value]
                defiende = self.jugadores[Turno.Jugador1.value]

            self.mostrar_turno()
            ataque_elegido, tipo_elemento_ataque = self.elegir_ataque(ataca)
            defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

            for jugador in self.jugadores:
                if jugador.vida == 0:
                    salir = "si"

            self.turno = Turno( (self.turno.value + 1) % 2 )
            print("***********atacante*************")
            print(ataca)
            print("***********defensor*************")
            print(defiende)

    def cargarjuego(self):
        pass


if __name__ == '__main__':
    b = Battle()

    elementos1 = [Elemento.AIRE, Elemento.TIERRA]
    nombre1 = "suri"

    elementos2 = [Elemento.AIRE, Elemento.AGUA]
    nombre2 = "pini"

    m1 = Monstruo(nombre1, elementos1)
    m2 = Monstruo(nombre2, elementos2)

    b.jugadores.append(m1)
    b.jugadores.append(m2)

    b.turno = Turno.Jugador1

    b.comenzarpelea()



