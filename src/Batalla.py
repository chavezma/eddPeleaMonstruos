from Elemento import Turno
from Elemento import Elemento
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
		return "Batalla Turno = [" + str(self.turno) + "] - Judador [" + str(self.jugador) + "]"

	def mostrar_turno(self, mostrartitulo):
		mostrartitulo
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
		
	def config_jugadores(self, mostrartitulo):
		idx_jugador = 0

		for idx_jugador in range(1, 3):
			mostrartitulo()
			print("\n")
			print("****  Cargando informacion del jugador " + str(idx_jugador) + " ****")
			self.jugadores.append(self.crear_monstruo())

		for jugador in self.jugadores:
			print(jugador)

		input("...")

	def comenzarpelea(self):
		pass
		
	def cargarjuego(self):
		pass


if __name__ == '__main__':
	b = Battle()

	def mos():
		print("aux")

	print(b.crear_monstruo())
	print(b.crear_monstruo())



