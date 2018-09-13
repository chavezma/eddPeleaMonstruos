import os

class Consola:

    def __init__(self):
        print("Que comiencen los juegos.")

    def mostrar_titulo(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\t**********************************************")
        print("\t***  Greeter - Hello old and new friends!  ***")
        print("\t**********************************************")

    def mostrar_menu(self):
        print("\n")
        print("[1] Nuevo Juego.")
        print("[2] Cargar.")
        print("[q] Salir.")

        return input("Elegir una opción: ")

    def obt_juegos_guardados(self):
        # Buscar el archivo batalla.save para dar a elegir que juego jugar.
        juegos = ["partida hoy", "partida lunes", "partida domingo"]
        idxjuego = -1
        idx = 1
        print("\nEstos son los juegos guardados.\n")
        for juego in juegos:
            print("[" + idx + "] " + juego)
        print("[0] Atras")

        while idxjuego < 0 & idxjuego > 2:
            idxjuego = input("Elegir una juego: ")

        if idxjuego > 0:
            print("Juego elegido " + juegos[idxjuego])
        else:
            print("eligio atras")

if __name__ == '__main__':
    myconsola = Consola()
    opcion = ''
    myconsola.mostrar_titulo()
    while opcion != 'q':
        opcion = myconsola.mostrar_menu()
        # Respond to the user's choice.
        myconsola.mostrar_titulo()
        if opcion == '1':
            print("Arrancamos juego nuevo")
        elif opcion == '2':
            myconsola.obt_juegos_guardados()
        elif opcion == 'q':
            print("\nEspero te hayas divertido.")
        else:
            print("\nLa opcion elegida no es valida.\n")
