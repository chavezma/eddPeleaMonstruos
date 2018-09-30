import os
import sys
import pickle
from Consola import Consola
from Batalla import Batalla
from Monstruo import Monstruo
from Elemento import Elemento
from Elemento import Turno
from JuegoExcepciones import JuegoGuardarException
from JuegoExcepciones import JuegoGuardadoExisteException
from JuegoExcepciones import JuegoCrearMonstruoException
from JuegoExcepciones import JuegoMenuPrincipalException
from JuegoExcepciones import JuegoOpcionInvalidaException


class Juego(Consola):
    batalla = Batalla()
    estado = ""

    def __init__(self):
        self.batalla = Batalla()
        self.estado = "Menu Principal"
        self.dict_opciones_menu_principal = {1: "Nuevo Juego", 2: "Continuar", 3: "Cargar Juego", 4: "Salir"}
        self.dict_opciones_elementos = {1: Elemento.AIRE, 2: Elemento.TIERRA, 3: Elemento.AGUA, 4: Elemento.FUEGO,
                                        5: "Atras"}

    def validar_nombre(self, cadena):
        for char in cadena:
            if not char.isalnum() and char is not '_':
                return False

        return True

    def juegos_guardados(self):
        dict_juegos_guardados = dict()
        total_juegos = 1
        # Buscar el archivo batalla.save para dar a elegir que juego jugar.
        for files in os.walk(".\\savedgames"):
            for filename in files:
                for file in filename:
                    if file.endswith(".save"):
                        dict_juegos_guardados[total_juegos] = file
                        total_juegos = total_juegos + 1

        dict_juegos_guardados[total_juegos] = "Atras"

        return dict_juegos_guardados

    def guardar_juego(self):
        archivo = ""
        print("\tEl nombre de archivo, debe ser sin extension, solo se aceptan alfanumericos y guion bajo\n")
        print("\tDejar vacío para volver al menu principal\n")
        archivo = input("\tIngrese el nombre: ")

        if len(archivo) == 0:
            raise JuegoMenuPrincipalException

        if self.validar_nombre(archivo):
            input("\n\tEl formato es incorrecto, por favor vuelva a intentarlo")
            raise JuegoGuardarException

        exists = os.path.isfile('.//savedgames//' + archivo + ".save")

        if exists:
            input("El archivo ya existe, utilice otro nombre.")
            raise JuegoGuardadoExisteException
        else:
            with open('.//savedgames//' + archivo + ".save", 'wb') as output:
                pickle.dump(self.batalla, output, pickle.HIGHEST_PROTOCOL)

        print("\n\t\tarchivo guardado con exito.")
        input("\t\tPresione cualquier tecla para continuar...")

    def cargar_juego(self):

        dict_juegos = self.juegos_guardados()

        try:
            opcion = self.pedir_opcion_menu(dict_juegos)
        except (ValueError, TypeError):
            raise JuegoOpcionInvalidaException

        if opcion == "Atras":
           raise JuegoMenuPrincipalException
        else:
            print("\tJuego elegido " + opcion)
            with open('.//savedgames//' + opcion, 'rb') as load:
                self.batalla = pickle.load(load)
                input("\n\t\tPresionar cualquier tecla para continuar...")

    def print_elementos(self, nro_elemento):
        if nro_elemento == 1:
            elem = "primer"
        elif nro_elemento == 2:
            elem = "segundo"
        else:
            raise JuegoOpcionInvalidaException

        print("\tElija su " + elem + " elemento")

    def crear_monstruo(self):

        id_jugador = len(self.batalla.jugadores) + 1
        elementos = []

        self.titulo()

        print("\n\t\t****  Cargando informacion del jugador " + str(id_jugador) + " ****")
        nombre = self.pedir_nombre()

        while len(elementos) < 2:
            try:

                self.print_elementos(len(elementos) + 1)
                opcion = self.pedir_opcion_menu(self.dict_opciones_elementos)

                if opcion == "Atras":
                    raise JuegoMenuPrincipalException
                else:
                    elementos.append(Elemento(opcion))

            except JuegoOpcionInvalidaException:
                input("\t\tOpcion invalida, reiniciando creacion de monstruo...")
                raise JuegoCrearMonstruoException

        return Monstruo(id_jugador, nombre, elementos)

    def elegir_ataque(self, jugador):
        dict_opciones_ataque = jugador.ataques_posibles()

        idxopelegida = len(dict_opciones_ataque) + 1

        dict_opciones_ataque[idxopelegida] = "Guardar"
        idxopelegida += 1
        dict_opciones_ataque[idxopelegida] = "Menu Principal"

        return dict_opciones_ataque

    def resumen_danio(self, monstruo):
        self.batalla.calculo_danio
        print("\n\t\tDanio calculado por Jugador " + str(monstruo.id_jugador) + "")
        print("\t\t[Danio Total = Danio Base + Plus Ataque - Plus Defensa]")
        print("\t\t[ " + str(self.batalla.calculo_danio[0]) + " = " + str(self.batalla.calculo_danio[1]) + " + " + str(self.batalla.calculo_danio[2]) + " - " + str(self.batalla.calculo_danio[3]) + "]")
        print("\t\tPunto de vida: [" + str(monstruo.vida) + "]")
        input("")


if __name__ == '__main__':
    myJuego = Juego()

    try:
        while True:
            myJuego.titulo()

            if myJuego.estado == "Menu Principal":
                try:
                    myJuego.estado = myJuego.pedir_opcion_menu(myJuego.dict_opciones_menu_principal)
                except JuegoOpcionInvalidaException:
                    myJuego.estado = "Menu Principal"
                except JuegoMenuPrincipalException:
                    myJuego.estado = "Menu Principal"

                continue

            elif myJuego.estado == "Nuevo Juego":
                try:

                    while len(myJuego.batalla.jugadores) < 2:
                        myJuego.batalla.jugadores.append(myJuego.crear_monstruo())

                except JuegoCrearMonstruoException:
                    myJuego.estado = "Nuevo Juego"
                    continue
                except JuegoMenuPrincipalException:
                    myJuego.estado = "Menu Principal"
                    continue

                myJuego.estado = "Continuar"
                continue

            elif myJuego.estado == "Guardar":

                try:
                    myJuego.guardar_juego()
                    myJuego.estado = "Continuar"
                except JuegoGuardadoExisteException:
                    myJuego.estado = "Guardar"
                    continue
                except JuegoGuardarException:
                    myJuego.estado = "Guardar"
                    continue
                except JuegoMenuPrincipalException:
                    myJuego.estado = "Menu Principal"
                    continue
                continue

            elif myJuego.estado == "Cargar Juego":

                try:
                    myJuego.cargar_juego()
                except JuegoOpcionInvalidaException:
                    myJuego.estado = "Cargar Juego"
                    continue
                except JuegoMenuPrincipalException:
                    myJuego.estado = "Menu Principal"
                    continue

                myJuego.estado = "Continuar"
                continue

            elif myJuego.estado == "Continuar":

                mAt = myJuego.batalla.obtener_atacante()
                mDf = myJuego.batalla.obtener_defensor()

                myJuego.mostrar_turno(myJuego.batalla.turno)
                dic_ataque = myJuego.elegir_ataque(mAt)
                opcion = myJuego.pedir_opcion_menu(dic_ataque)

                if opcion in ["Menu Principal", "Guardar"]:
                    myJuego.estado = opcion
                    continue

                myJuego.batalla.pelear(opcion.tipo, opcion.elem)
                myJuego.resumen_danio(mDf)

                if myJuego.batalla.turno == Turno.Jugador2:
                    myJuego.batalla.ronda += 1
                    print("\tResumen ronda:")
                    print(myJuego.batalla)
                    input()

                myJuego.batalla.actualizar_turno()

            elif myJuego.estado == "Salir":
                break

            else:
                myJuego.estado = "Menu Principal"

        print("\nEspero te hayas divertido.\n")

    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError as error:
        # Output expected EOFErrors.
        print(error)
        sys.exit(0)

