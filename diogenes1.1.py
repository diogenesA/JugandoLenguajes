import sys



class String:

    def __init__(self, cadena):
        
        self.cadena              = cadena
        self.componentes         = [',','}','{']
        self.operadores          = ['.','&','-','*']
        self.lista_general       = []
        self.lista_interseccion  = []
        self.lista_diferencia    = []
        self.lista_distribucion  = []
        self.lista_concatenacion = []
        

    def cadena_lista(self):

        aux=''
        
        for e in self.cadena:
            if e in self.componentes:
                self.lista_general.append(aux)
                aux=''
            else:
                aux+=e
    
    def dividir_cadena(self):

        self.lista1 = []
        self.lista2 = []

        for e in self.lista_general:
            if e in self.operadores:
                pos = self.lista_general.index(e)
                self.lista1 = self.lista_general[2:pos]
                self.lista2 = self.lista_general[pos+1:len(self.lista_general)]
                    
    def concatenacion(self):

        self.lista_concatenacion = self.lista1 + self.lista2
        print("Concatenación: ", self.notacion(self.lista_concatenacion))
    
    def notacion(self,lista):
        
        nota='{'
        c=1
        for u in lista:    
            nota+=str(u)
            if c<len(lista):
                nota+=str(',')
            c+=1
        return nota+'}'

    def interseccion(self):

        for x in self.lista1:
            for y in self.lista2:
                if x == y:
                    self.lista_interseccion.append(x)
        print("Interseción: ",(self.notacion(self.lista_interseccion)))
    
    def diferencia(self):
            
        for x in self.lista1:
            n_veces = False
            for y in self.lista2:
                if x==y:
                    n_veces=True
            if not n_veces:
                self.lista_diferencia.append(x)
        print("Diferencia: ",self.notacion(self.lista_diferencia))
    
    def distribucion(self):
        
        for x in self.lista1:
            for y in self.lista2:
                self.lista_distribucion.append(x+y)
        print("Distribuccion: ",self.notacion(self.lista_distribucion))
    
    def cardinal(self,cadena):
        c=1
        for e in cadena:
           if e==',':
               c+=1
        return c


    def potencia(self,potencia,cadena):
        
        n=0
        ant = []
        act = []

        while n < potencia:
            listanueva = []
            for x in ant:
                for y in cadena:
                    listanueva.append(x+y)
            ptr = cadena 
            cadena = ant + listanueva
            ant = act
            n+=1
        print(self.cadena)


if __name__ == '__main__':

    if len(sys.argv) == 1:
       print("ingrese la expresión...")
    else:
       entrada = sys.argv
       s = String(str(entrada))
       s.cadena_lista()
       s.dividir_cadena()
       s.distribucion()

       """s.interseccion()
       s.concatenacion()
       s.distribucion()"""


