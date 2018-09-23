import os
import sys
import pickle
from Batalla import Batalla
from Monstruo import Monstruo
from Elemento import Elemento
from JuegoExcepciones import JuegoGuardarException
from JuegoExcepciones import JuegoCrearMonstruoException

class Juego:
    batalla = Batall()
    estado = ""

    def __init__(self):
        self.batalla = Batalla()
        self.estado = "activo"

    def menu_principal(self):
        self.juego_titulo()
        return self.juego_menu()


    def juego_titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***********  Batalla de monstruos  ***********")
        print("\t**********************************************")
        return

    def juego_menu(self):
        idxopcion = 0
        opcorrectas = [1,2,3,4]
        lstmenu = ["nuevo", "continuar", "cargar", "salir"]
        print("\n")
        print("\t[1] Nuevo Juego.")
        print("\t[2] Continuar.")
        print("\t[3] Cargar.")
        print("\t[4] Salir.")

        while idxopcion not in opcorrectas:
            try:
                idxopcion = int(input("\n\tElegir una opción: "))
            except ValueError:
                idxopcion = 0

        return lstmenu[idxopcion-1]

    def juegos_guardados(self):
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

    def guardar_juego(self):
        archivo = ""
        archivo = input("\n\t\tElija un nombre (sin extension) para el archivo: ")

        exists = os.path.isfile('.//savedgames//' + archivo + ".save")
        if exists:
            print("El archivo ya existe, utilice otro nombre.")
            raise ValueError
        else:
            with open('.//savedgames//' + archivo + ".save", 'wb') as output:
                pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

        print("\n\t\tarchivo guardado con exito.")
        input("\t\tPresione cualquier tecla para continuar...")

    def cargar_juego(self):
        lstjuegos = []
        total_juegos = 0
        opcion_ok = "no"
        idxjuego = 0

        lstjuegos = self.juegos_guardados()

        try:
            idxjuego = int(input("Elegir opcion: "))
            opcion_ok = "si"
        except ValueError:
            raise JuegoOpcionInvalidaException

        if idxjuego == 0:
           raise JuegoMenuPrincipalException
        else:
            print("\tJuego elegido " + lstjuegos[idxjuego-1])
            with open('.//savedgames//' + lstjuegos[idxjuego-1], 'rb') as load:
                batalla = pickle.load(load)
                input("\n\t\tPresionar cualquier tecla para continuar...")
                return batalla

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

    def crear_monstruo(self):
        id_jugador = len(self.batalla.jugadores) + 1
        elementos = []
        choose = 0
        nombre = ""
        estado = ""
        idx_elemento = 0

        self.juego_titulo()
        print("\n\t\t****  Cargando informacion del jugador " + str(id_jugador) + " ****")

        nombre = str(input("\tIngrese su nombre: "))

        try:
            for idx_elemento in range(1, 3):
                self.print_elementos(idx_elemento)
                choose = int(input("\tOpcion: "))
                elementos.append(Elemento(choose))

        except ValueError:
            input("\t\tOpcion invalida, reiniciando creacion de monstruo...")
            raise JuegoCrearMonstruoException

        return Monstruo(id_jugador, nombre, elementos)

if __name__ == '__main__':
    myJuego = Juego()
    opcion = "menu"
    opcorrecta = 0
    estado = ""

    try:
        while myJuego.estado == "activo":
            if opcion == "menu":
                opcion = myJuego.menu_principal()
            elif opcion == "nuevo":
                try:
                    while len(myJuego.batalla.jugadores) < 2:
                        myJuego.batalla.jugadores.append(myJuego.crear_monstruo())
                except JuegoCrearMonstruoException:
                    opcion = "nuevo"
                    continue

                opcion = "continuar"

            elif opcion == "guardar":
                myJuego.guardar_juego()
                opcion = "continuar"
            elif opcion == "cargar":
                myJuego.juego_titulo()
                try:
                    myJuego.batalla = myJuego.cargar_juego()
                except JuegoOpcionInvalidaException:
                    opcion = "cargar"
                    continue
                except JuegoMenuPrincipalException:
                    opcion = "menu"
                    continue
                opcion = "continuar"
            elif opcion == "continuar":
                if len(myJuego.batalla.jugadores) < 2:
                    print("\n\t\tSe eligio continuar sin crear los 2 monstruos...")
                    input("\n\t\tPresione cualquier tecla para volver al menu principal")
                    opcion = "menu"
                    continue
                myJuego.juego_titulo()
                opcion = myJuego.batalla.pelear()
            elif opcion == "salir":
                myJuego.estado = "noactivo"

    except KeyboardInterrupt:
        sys.exit(0)
