from enum import Enum


class Turno(Enum):
	Jugador1 = 0
	Jugador2 = 1

	# def __str__(self):
	# 	return str(self.value)


class Elemento(Enum):
	AIRE = 1
	TIERRA = 2
	AGUA = 3
	FUEGO = 4

	def get_elemento(self, idx):
		"""Dispatch method"""
		method_name = 'elemento_' + str(idx)
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Elemento invalido")
		# Call the method as we return it
		return method()

	def elemento_1(self):
		return Elemento.AIRE

	def elemento_2(self):
		return Elemento.TIERRA

	def elemento_3(self):
		return Elemento.AGUA

	def elemento_4(self):
		return Elemento.FUEGO

# matrizBonificaciones = [[1, 0.8, 1.2, 1], [1.2, 1, 0.8, 1], [1, 0.8, 1, 1.2], [0.8, 1.2, 1, 1]]

# def get_bonificacion_ataque(fila, columna):
#	# eturn matrizBonificaciones[fila][columna]
#	pass
