import os
import sys
from JuegoExcepciones import *


class Consola():

    def titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***********  Batalla de monstruos  ***********")
        print("\t**********************************************")
        return

    def mostrar_turno(self, turno):
        print("\t****  Es el turno de [" + str(turno) + "] ****")
        print("\t**********************************************")

    # def pedir_nombre(self):
    #     try:
    #         nombre=input("\n\tIngrese su nombre: ")
    #
    #         if not nombre:
    #             input("\n\tNo se puede ingresar un nombre vacio...\n\tPresione cualquier tecla para volver al menu principal")
    #             raise JuegoMenuPrincipalException
    #
    #     except KeyboardInterrupt:
    #         raise JuegoMenuPrincipalException

    def dibujar_menu(self, dictmenu):
        idxopcion = 0
        #self.titulo()
        print("\n")
        for op in dictmenu:
            print("\t[" + str(op) + "] " + str(dictmenu[op]) + ".")

    def pedir_opcion_menu(self, dictopcion):
        try:
            self.dibujar_menu(dictopcion)
            out = input("\n\tElegir una opción: ")

            if len(out) == 0:
                input("\n\tNo se ha ingresado opcion, se retorna al menu principal")
                return "Menu Principal"
            else:
                idxopcion = int(out)

            if idxopcion not in dictopcion.keys():
                raise JuegoOpcionInvalidaException

        except (ValueError, TypeError):
            raise JuegoOpcionInvalidaException
        except KeyboardInterrupt:
            raise JuegoMenuPrincipalException
        except EOFError:
            return "Menu Principal"

        return dictopcion[idxopcion]



