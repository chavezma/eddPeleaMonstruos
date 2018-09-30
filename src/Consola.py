import os
import sys
from JuegoExcepciones import JuegoOpcionInvalidaException
from JuegoExcepciones import JuegoMenuPrincipalException


class Consola():

    def titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***********  Batalla de monstruos  ***********")
        print("\t**********************************************")
        return

    def dibujar_menu(self, dictmenu):
        idxopcion = 0
        #self.titulo()
        print("\n")
        for op in dictmenu:
            print("\t[" + str(op) + "] " + str(dictmenu[op]) + ".")

    def pedir_opcion_menu(self, dictopcion):
        try:
            self.dibujar_menu(dictopcion)
            idxopcion = int(input("\n\tElegir una opción: "))

            if idxopcion not in dictopcion.keys():
                raise JuegoOpcionInvalidaException

        except (ValueError, TypeError):
            raise JuegoOpcionInvalidaException
        except KeyboardInterrupt:
            raise JuegoMenuPrincipalException
        except EOFError:
            return "Menu Principal"

        return dictopcion[idxopcion]

    def mostrar_turno(self, turno):
        print("\t****  Es el turno de [" + str(turno) + "] ****")
        print("\t**********************************************")

    def pedir_nombre(self):
        try:
            return input("\n\tIngrese su nombre: ")
        except KeyboardInterrupt:
            raise JuegoMenuPrincipalException


if __name__ == '__main__':
    dict_opciones_menu_principal = {1: "Nuevo Juego", 2: "Continuar", 3: "Cargar Juego", 4: "Salir"}
    dict_opciones_elementos = {1: "AIRE", 2: "TIERRA", 3: "AGUA", 4: "FUEGO"}
    dict_opciones_ataque = {1: "AIRE", 2: "TIERRA", 3: "AGUA", 4: "FUEGO"}

    c = Consola()
    c.pedir_opcion(dict_opciones_menu_principal)

    c.pedir_opcion(dict_opciones_elementos)
