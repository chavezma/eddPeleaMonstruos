from Elemento import Elemento
from Elemento import tipo_ataque

class Monstruo:
	
	# Un monstruo recibe el nombre y una lista de elementos
	def __init__(self, nombre, elementos):
		self.nombre = nombre
		self.elementos = elementos
		self.vida = 100
		self.max_cant_esp_att = 4
		self.cant_esp_att = 0

	def __repr__(self):
		printelem = "["
		for x in self.elementos:
			printelem += str(x) + ","
		printelem += "]"

		return "Monstruo = [" + self.nombre + "] vida [" + str(self.vida) + "] - elementos " + printelem
		# return self.nombre + ";" + str(self.vida) + ";" + printelem

	def recibir_ataque(self, t_ataque, t_elem_ataque):
		fortalezas = []
		debilidades = []
		lista = []
		danio_total = 100
		danio_base = 0
		plus_ataque = 0
		plus_defensa = 0

		if t_ataque == tipo_ataque.NORMAL:
			danio_base = 10
		elif t_ataque == tipo_ataque.ESPECIAL:
			danio_base = 15
			for mi_elem in self.elementos:
				debilidades.append( Elemento(1).tiene_plus_ataque(mi_elem) )

			if t_ataque in debilidades:
				plus_ataque = danio_base*1.2

			for mi_elem in self.elementos:
				fortalezas.append( Elemento(1).tiene_plus_defensa(mi_elem) )

			if t_ataque in fortalezas:
				plus_defensa = danio_base*0.8

		danio_total = danio_base + plus_ataque - plus_defensa

		self.vida -= danio_total

		print("mis elementos")
		print(self.elementos)
		print("plus defensivo contra")
		print(fortalezas)
		print("el ataque es fuerte contra")
		print(debilidades)

		print("danio_total " + str(danio_total))


if __name__ == '__main__':
	elementos = [Elemento.AIRE, Elemento.TIERRA]
	nombre = "suri"

	ataque = tipo_ataque.ESPECIAL
	t_at = Elemento.FUEGO

	m = Monstruo(nombre, elementos)

	m.recibir_ataque(ataque, t_at)

	print(m)