from enum import Enum

class Elemento(Enum):
     AIRE = 0
     TIERRA = 1
     AGUA = 2
     FUEGO = 3
	 
matrizBonificaciones = 	[
						 [1,0.8,1.2,1],
						 [1.2,1,0.8,1],
						 [1,0.8,1,1.2],
						 [0.8,1.2,1,1],
						]

def getBonificacionAtaque(fila, columna):
		return matrizBonificaciones[fila][columna]