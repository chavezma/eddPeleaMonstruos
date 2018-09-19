import os
import sys
import pickle
from Batalla import Batalla

class Juego:
    def __init__(self):
        print("Que comiencen los juegos.")

    def mostrar_titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***********  Batalla de monstruos  ***********")
        print("\t**********************************************")

    def mostrar_menu(self):
        opcion = 0
        print("\n")
        print("\t[1] Nuevo Juego.")
        print("\t[2] Cargar.")
        print("\t[3] Salir.")

        try:
            opcion = int(input("\n\tElegir una opción: "))
        except ValueError:
            return 0

        return opcion

    def mostrar_juegos_guardados(selfs):
        lstjuegos = []
        total_juegos = 0
        # Buscar el archivo batalla.save para dar a elegir que juego jugar.
        for files in os.walk(".\\savedgames"):
            for filename in files:
                for file in filename:
                    if file.endswith(".save"):
                        lstjuegos.append(file)

        total_juegos = len(lstjuegos)
        idx = 1
        print("\nEstos son los juegos guardados.\n")
        for juego in lstjuegos:
            print("\t[" + str(idx) + "] " + juego)
            idx = idx + 1
        print("\t[0] Atras")

        return lstjuegos

    def cargar_juego(self):
        lstjuegos = []
        total_juegos = 0
        opcion_ok = "no"
        idxjuego = 0

        try:
            lstjuegos = self.mostrar_juegos_guardados()

            while opcion_ok == "no":
                try:
                    idxjuego = int(input("Elegir opcion: "))
                    opcion_ok = "si"
                except ValueError:
                    input("\tOpcion invalida, favor de elegir nuevamente...")
                    continue

            if idxjuego == 0:
                print("\tEligio Atras")
                return Batalla(), "atras"
            else:
                print("\tJuego elegido " + lstjuegos[idxjuego-1])
                with open('.//savedgames//' + lstjuegos[idxjuego-1], 'rb') as load:
                    batalla = pickle.load(load)
                    input("\n\t\tPresionar cualquier tecla para continuar...")
                    return batalla, "jugar"

        except ValueError:
            input("\tOpcion invalida, favor de elegir nuevamente...")
            return batalla, "jugar"


if __name__ == '__main__':
    try:
        myJuego = Juego()
        opcion = 0
        opcorrecta = 0
        newbattle = Batalla()

        while opcion != 3:
            try:
                myJuego.mostrar_titulo()
                opcion = myJuego.mostrar_menu()

                if opcion == 1:

                    newbattle.config_jugadores(myJuego.mostrar_titulo)
                    newbattle.comenzarpelea(myJuego.mostrar_titulo)

                elif opcion == 2:
                    myJuego.mostrar_titulo()
                    newbattle, status = myJuego.cargar_juego()

                    if status == "atras":
                        continue
                    else:
                        newbattle.comenzarpelea(myJuego.mostrar_titulo)

                elif opcion == 3:
                    print("\nEspero te hayas divertido.")
                else:
                    print("\n\t\tLa opcion elegida no es valida.\n")
                    input("\t\tPresionar una tecla para continuar...")

            except ValueError:
                print("\noooooo.\n")
                input("....")

    except Exception as ex:
        print(ex)
        sys.exit(1)

