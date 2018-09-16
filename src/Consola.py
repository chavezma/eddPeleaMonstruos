import os
import sys
from Batalla import Battle


class Consola:
    def __init__(self):
        print("Que comiencen los juegos.")

    def mostrar_titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***********  Battala de monstruos  ***********")
        print("\t**********************************************")

    def mostrar_menu(self):
        print("\n")
        print("[1] Nuevo Juego.")
        print("[2] Cargar.")
        print("[q] Salir.")

        return input("Elegir una opción: ")

    def obt_juegos_guardados(self):
        try:
            # Buscar el archivo batalla.save para dar a elegir que juego jugar.
            juegos = ["partida hoy", "partida lunes", "partida domingo"]
            idx = 1
            print("\nEstos son los juegos guardados.\n")
            for juego in juegos:
                print("[" + str(idx) + "] " + juego)
                idx = idx + 1
            print("[0] Atras")

            idxjuego = int(input("Elegir opcion: "))
            while idxjuego < 0 or idxjuego > 2:
                input("Opcion invalida, favor de elegir nuevamente...")
                return 0

            if idxjuego == 0:
                print("Eligio Atras")
            else:
                print("Juego elegido " + juegos[idxjuego-1])
                input("")
            return 1

        except ValueError:
            input("Opcion invalida, favor de elegir nuevamente...")
            return 0


if __name__ == '__main__':
    try:
        myconsola = Consola()
        opcion = ''
        opcorrecta = 0

        while opcion != 'q':
            myconsola.mostrar_titulo()
            opcion = myconsola.mostrar_menu()

            if opcion == '1':
                print("Arrancamos juego nuevo")
                newbattle = Battle()
                print("Batalla")
                print(newbattle)
                input("press to contnue.")
                newbattle.config_jugadores(myconsola.mostrar_titulo)

            elif opcion == '2':
                opcorrecta = 0
                while opcorrecta == 0:
                    myconsola.mostrar_titulo()
                    opcorrecta = myconsola.obt_juegos_guardados()
            elif opcion == 'q':
                print("\nEspero te hayas divertido.")
            else:
                print("\nLa opcion elegida no es valida.\n")

    except Exception as ex:
        print(ex)
        sys.exit(1)

