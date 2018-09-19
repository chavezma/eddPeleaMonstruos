import pickle
import os
from Elemento import Turno
from Elemento import Elemento
from Elemento import tipo_ataque
from Monstruo import Monstruo
from JuegoExcepciones import JuegoSalirException
# Variables para iniciar-restaurar una batalla.

# Monstruo 1 [nombre, vida, elementos, cantAtaquesEsp, turno] 
# Monstruo 2 [nombre, vida, elementos, cantAtaquesEsp, turno]


class Batalla:
    def __init__(self):
        self.jugadores = []
        self.turno = Turno.Jugador1
        self.jugador = 1

    def print_elementos(self, nro_elemento):
        if nro_elemento == 1:
            elem = "primer"
        else:
            elem = "segundo"

        print("\t\tElija su " + elem + " elemento")
        print("\t\t[1] AIRE.")
        print("\t\t[2] TIERRA.")
        print("\t\t[3] AGUA.")
        print("\t\t[4] FUEGO.")

    def __repr__(self):
        monstruos = ""
        for m in self.jugadores:
            monstruos += str(m) + "\n"
        monstruos += "\tBatalla Turno = [" + str(self.turno) + "]"
        return monstruos

    def mostrar_turno(self):
        print("\t****  Es el turno de [" + str(self.turno) + "] ****")
        print("\t**********************************************")

    def crear_monstruo(self, idx_jugador):
        elemento = []
        nombre = ""
        ups = Elemento(1)

        nombre = str(input("\tIngrese su nombre:"))

        for idx_elemento in range(1, 3):
            self.print_elementos(idx_elemento)
            choose = int(input("\tOpcion:"))
            #print("\tEleccion realizada [" + str(choose) + "].")
            #input("\tpresionar algo....")
            elemento.append(Elemento(choose))

        return Monstruo(idx_jugador, nombre, elemento)

    def config_jugadores(self, mostrar_titulo):
        idx_jugador = 0

        for idx_jugador in range(1, 3):
            mostrar_titulo()
            print("\n\t****  Cargando informacion del jugador " + str(idx_jugador) + " ****")
            self.jugadores.append(self.crear_monstruo(idx_jugador))

        for jugador in self.jugadores:
            print(jugador)

        input("\t\tPresionar cualquier tecla para continuar...")

    def guardar_batalla(self):
        archivo = ""

        archivo = input("\n\t\tElija un nombre (sin extension) para el archivo")

        exists = os.path.isfile('.//savedgames//' + archivo)
        if exists:
            print("El archivo ya existe, utilice otro nombre.")
            raise ValueError
        else:
            with open('.//savedgames//' + archivo, 'wb') as output:
                pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

        print("archivo guardado con exito.")
        input("Presione cualquier tecla para continuar...")

    def elegir_ataque(self, jugador):

        lista_op_validas = [1, 2, 3, 4, 5, 6]
        idxopelegida = 0
        op_ok = "NO"

        while op_ok == "NO":
            idx_op = 1
            try:
                print("\t\tElija el tipo de ataque que desea utilizar")
                for elem in jugador.elementos:
                    print("\t\t[" + str(idx_op) + "] NORMAL tipo " + str(elem))
                    idx_op += 1

                if jugador.cant_esp_att < 4:
                    for elem in jugador.elementos:
                        print("\t\t[" + str(idx_op) + "] ESPECIAL tipo " + str(elem))
                        idx_op += 1

                print("\t\t[5] Guardar.")
                print("\t\t[6] Salir.")

                idxopelegida = int(input("\t\tElegir opcion: "))

                if idxopelegida in lista_op_validas:
                    op_ok = "SI"
                else:
                    raise ValueError("error al elegir ataque, restauro")

            except ValueError:
                raise ValueError("error al elegir ataque, restauro")

        if idxopelegida == 1:
            return tipo_ataque.NORMAL, jugador.elementos[0]
        elif idxopelegida == 2:
            return tipo_ataque.NORMAL, jugador.elementos[1]
        elif idxopelegida == 3:
            return tipo_ataque.ESPECIAL, jugador.elementos[0]
        elif idxopelegida == 4:
            return tipo_ataque.ESPECIAL, jugador.elementos[1]
        elif idxopelegida == 5:
            try:
                self.guardar_batalla()
                raise ValueError("Como eligio guardar, restauro")
            except ValueError:
                raise ValueError("Hubo un error al guardar, restauro")
        elif idxopelegida == 6:
            raise JuegoSalirException

    def comenzarpelea(self, mostrar_titulo):
        ataque_elegido = 0
        tipo_elemento_ataque = 0
        danio_total = 0
        calculo = ""
        restart = 0

        salir = "no"
        while salir == "no":
            mostrar_titulo()

            if restart == 0:
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
                restart = 1
                continue
            except JuegoSalirException:
                salir = "si"
                continue

            danio_total, calculo = defiende.recibir_ataque(ataque_elegido, tipo_elemento_ataque)

            print("\n\t\tDanio calculado por Jugador " + str(defiende.id_jugador) + "")
            print("\t\t[Danio Total = Danio Base + Plus Ataque - Plus Defensa]")
            print("\t\t" + calculo)
            print("\t\tPunto de vida: [" + str(defiende.vida) + "]")

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
