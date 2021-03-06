from NodoOrtogonal import Nodo

class Lista_V:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def insertar(self, dato, x, y):
        nodo_nuevo = Nodo(dato, x, y)
        if self.vacia() == True:
            self.primero = self.ultimo = nodo_nuevo

        elif nodo_nuevo.y < self.primero.y:
            self.agregar_inicio(dato, x, y)

        elif nodo_nuevo.y > self.ultimo.y:
            self.agregar_final(dato, x, y)
        #else:
            #print('Hello World')
            #self.agregar_medio()


    def agregar_inicio(self, dato, x, y):
        aux = Nodo(dato, x, y)
        self.primero.arriba = aux
        aux.abajo = self.primero
        self.primero = aux
        

    def agregar_final(self, dato, x, y):
        aux = Nodo(dato,x,y)
        self.ultimo.abajo = aux
        aux.arriba = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        current = self.primero

        while current: # mientras que aux != None (mientras que el nodo no este vacio)
            print('(',current.dato, ' x:' ,current.x, ' y:' ,current.y,')', end = "  =>  ")
            current = current.abajo

    
    def recorrer_fin(self):
        current = self.ultimo

        while current: # mientras que aux != None
            print('(',current.dato, ' x:' ,current.x, ' y:' ,current.y,')', end = "  =>  ")
            current = current.arriba
        



