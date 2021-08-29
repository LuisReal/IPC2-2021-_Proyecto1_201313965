from NodoOrtogonal import Nodo

class Lista_H:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def insertar(self,dato,x,y):
        nodo_nuevo = Nodo(dato, x, y)
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato, x, y)

        elif nodo_nuevo.x < self.primero.x:
            self.agregar_inicio(dato, x, y)

        elif nodo_nuevo.x > self.ultimo.x:
            self.agregar_final(dato, x, y)
        #else:
            #print('Hello World')
            #self.agregar_medio()


    def agregar_inicio(self, dato, x, y):
        aux = Nodo(dato, x, y)
        self.primero.izquierda = aux
        aux.derecha = self.primero
        self.primero = aux
        

    def agregar_final(self, dato, x, y):
        aux = Nodo(dato,x,y)
        self.ultimo.derecha = aux
        aux.izquierda = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        current = self.primero

        while current: # mientras que aux != None (mientras que el nodo no este vacio)
            print('(',current.dato, ' x:' ,current.x, ' y:' ,current.y,')', end = "  =>  ")
            current = current.derecha

    
    def recorrer_fin(self):
        current = self.ultimo

        while current: # mientras que aux != None
            print('(',current.dato, ' x:' ,current.x, ' y:' ,current.y,')', end = "  =>  ")
            current = current.izquierda