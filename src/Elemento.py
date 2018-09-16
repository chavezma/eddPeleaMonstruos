from enum import Enum

class tipo_ataque(Enum):
	NORMAL = 1
	ESPECIAL = 2

	def get_ataque(self, idx):
		"""Dispatch method"""
		method_name = 'ataque_' + str(idx)
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Ataque invalido")
		# Call the method as we return it
		return method()

	def ataque_1(self):
		return tipo_ataque.NORMAL

	def ataque_2(self):
		return tipo_ataque.ESPECIAL


class Turno(Enum):
	Jugador1 = 0
	Jugador2 = 1


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

	def tiene_plus_ataque(self, elemento):
		# Quien tiene plus de ataque contra param
		# AGUA --> AIRE --> TIERRA --> FUEGO --> AGUA
		if elemento == Elemento.AGUA:
			return Elemento.AIRE
		elif elemento == Elemento.AIRE:
			return Elemento.TIERRA
		elif elemento == Elemento.TIERRA:
			return Elemento.FUEGO
		if elemento == Elemento.FUEGO:
			return Elemento.AGUA

	def tiene_plus_defensa(self, elemento):
		# AGUA --> TIERRA --> AIRE --> FUEGO --> AGUA
		if elemento == Elemento.AGUA:
			return Elemento.TIERRA
		elif elemento == Elemento.TIERRA:
			return Elemento.AIRE
		if elemento == Elemento.AIRE:
			return Elemento.FUEGO
		elif elemento == Elemento.FUEGO:
			return Elemento.AGUA

# matrizBonificaciones = [[1, 0.8, 1.2, 1], [1.2, 1, 0.8, 1], [1, 0.8, 1, 1.2], [0.8, 1.2, 1, 1]]

# def get_bonificacion_ataque(fila, columna):
#	# eturn matrizBonificaciones[fila][columna]
#	pass

if __name__ == '__main__':
	el = Elemento(1)

	print(el)

	if el == Elemento.AIRE:
		print("es aire")

