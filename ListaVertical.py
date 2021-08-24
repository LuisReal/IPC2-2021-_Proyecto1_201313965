from NodoOrtogonal import Nodo

class Lista:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregar_final(self,dato, x, y, arriba, abajo, izquierda, derecha):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato, x, y, arriba, abajo, izquierda, derecha)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato, x, y, arriba, abajo, izquierda, derecha)
            self.ultimo.anterior = aux

        self.size +=1 

    def agregar_inicio(self, dato, x, y, arriba, abajo, izquierda, derecha):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato, x, y, arriba, abajo, izquierda, derecha)
        else:
            aux = Nodo(dato, x, y, arriba, abajo, izquierda, derecha)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        
        self.size += 1

    def recorrer_inicio(self):
        aux = self.primero

        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def recorrer_fin(self):
        aux = self.ultimo

        while aux:
            print(aux.dato)
            aux = aux.anterior



