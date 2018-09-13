import os

# Variables para iniciar-restaurar una batalla.

# Monstruo 1 [nombre, vida, elementos, cantAtaquesEsp, turno] 
# Monstruo 2 [nombre, vida, elementos, cantAtaquesEsp, turno]

class Batalla():
	
	def __init__(self):
		Jugadores = []
		
	def mostrarTitulo():
		os.system('cls' if os.name == 'nt' else 'clear')

		print("\t**********************************************")
		print("\t***  Batalla de Monstruos  ***")
		print("\t**********************************************")
	
	def mostrarTurno():
		print("\t***  Es el turno de [" + getTurno() + "] *****")
		print("\t**********************************************")
		
	def configJugador():
		#Pedir nombre jugador 1
		#Pedir elemento 1
		#Pedir elemento 2
		#definimos vida
		#ataques restantes
		#Pedir nombre jugador 2
		#Pedir elemento 1
		#Pedir elemento 2
		pass
	
	def getTurno():
		Jugador = for x in Jugadores if x.Turno()
		return Jugador.nombre()
		
	def comenzarPelea():
		pass
		
	def cargarJuego():
		pass
		
	def getNombreGanador() {
		return this.defensor.getNombre();
	}



	

	

	

	

}