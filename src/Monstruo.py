from Elemento import Elemento

class Monstruo:
	
	# Un monstruo recibe el nombre y una lista de elementos
	def __init__(self, nombre, elementos):
		self.nombre = nombre
		self.elementos = elementos
		self.vida = 100

	def __repr__(self):
		printelem = ""
		for x in self.elementos:
			printelem += "[" + str(x) + "]\n"

		return "Monstruo = [" + self.nombre + "] - elementos \n" + printelem

	def get_Elementos(self):
		return self.elementos

	def restar_vida(self, danioataque):
		self.vida -= danioataque
		if self.vida < 0:
			self.vida = 0

	def get_vida(self):
		return self.vida
