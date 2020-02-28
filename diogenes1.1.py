import sys


class Potencia(object):

	def __init__(self, expresion):

		self.expresion   = expresion
		self.n_potencia    = int(self.expresion[-1])
		self.componentes = ['{','}','^',',']
		self.cadena      = []
		self.operar      = []


	def descomponer_cadena(self):
		
		aux = ''
		c=0

		for e in self.expresion:

			if e in self.componentes:
				self.cadena.append(aux)
				aux=''
			else:
				aux+=e

	def potencia(self):

		n=0
		
		act = []
		self.operar = self.cadena[1:len(self.cadena)]
		ant = self.operar

		while n < self.n_potencia:

			listanueva = []
			for x in ant:
				for y in self.operar:
					listanueva.append(x+y)
			act = self.operar 
			self.operar = ant + listanueva
			ant = act
			n+=1

		print(self.operar)
       




if __name__ == '__main__':
    
    if len(sys.argv) == 1:
       print("ingrese la expresión...")
    else:
       entrada = sys.argv[1]
       p = Potencia(str(entrada))
       p.descomponer_cadena()
       p.potencia()
       