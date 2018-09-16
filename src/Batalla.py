from Elemento import Turno
from Elemento import Elemento
from Monstruo import Monstruo
# Variables para iniciar-restaurar una batalla.

# Monstruo 1 [nombre, vida, elementos, cantAtaquesEsp, turno] 
# Monstruo 2 [nombre, vida, elementos, cantAtaquesEsp, turno]


class Battle:
	def __init__(self):
		self.jugadores = [Monstruo, Monstruo]
		self.turno = Turno.Jugador2
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
		
	def config_jugadores(self, mostrartitulo):
		idx_jugador = 0
		idx_elemento = 1
		mostrartitulo()
		print("****  Cargando informacion del jugador 1 ****")
		elemento = []
		#Pedir nombre jugador 1
		#Pedir elemento 1
		#Pedir elemento 2
		nombre = ""
		ups=Elemento(1)
		nombre = str(input("Jugador " + str(idx_jugador + 1) + " ingrese su nombre:"))
		self.print_elementos(idx_elemento)
		choose = int(input("Opcion:"))
		print("eligio 1 [" + str(choose) + "].")
		input("....")
		elemento.append(ups.get_elemento(1))
		idx_elemento = idx_elemento + 1
		self.print_elementos(idx_elemento)
		choose = int(input("Opcion:"))
		print("eligioe 2 [" + str(choose) + "].")
		input("....")
		elemento.append(ups.get_elemento(2))
		self.jugadores[idx_jugador] = Monstruo(nombre, elemento)

		m = Monstruo(nombre, elemento)

		print(m)

		#definimos vida
		#ataques restantes
		#Pedir nombre jugador 2
		#Pedir elemento 1
		#Pedir elemento 2

	def comenzarpelea(self):
		pass
		
	def cargarjuego(self):
		pass
		
	def getganador(self):
		pass


if __name__ == '__main__':
	b = Battle()

	def mos():
		print("aux")

	b.config_jugadores(mos)


