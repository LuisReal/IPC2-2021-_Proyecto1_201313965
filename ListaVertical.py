from NodoOrtogonal import Nodo

class Lista:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def insertar(self,dato,x,y):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato, x, y)

        elif Nodo(dato,x,y).y < self.primero.y:
            self.agregar_inicio()

        elif Nodo(dato,x,y).y > self.ultimo.y:
            self.agregar_final()
        else:
            self.agregar_medio()


    

    def agregar_inicio(self, dato, x, y):
        aux = Nodo(dato, x, y)
        self.primero.arriba = aux
        aux.abajo = self.primero
        self.primero = aux
        
        

    def agregar_medio(self,dato, x, y):
        temp1 = Nodo(dato, x, y)
        temp2 = Nodo(dato, x, y)

        temp1 = self.primero
        while temp1.y < Nodo(dato,x,y).y:
            temp1 = temp1.abajo
        
        temp2 = temp1.arriba
        temp2.abajo = Nodo(dato, x, y)
        Nodo(dato,x,y).abajo = temp1
        Nodo(dato,x,y).arriba = temp2
        temp1.arriba = Nodo(dato,x,y)
        
           

    def agregar_final(self,dato, x, y):
        aux = Nodo(dato,x,y)
        self.ultimo.abajo = aux
        aux.arriba = self.ultimo
        self.ultimo = aux
            
        

    def recorrer_inicio(self):
        current_ar = self.primero
        current_ab = self.primero
        current_ai = self.primero
        current_ad = self.primero

        while current_ab: # mientras que aux != None (mientras que el nodo no este vacio)
            if current_ab.x < current_ab.derecha.x:
                print('(',current_ab.dato, ' x:' ,current_ab.x, ' y:' ,current_ab.y,')', end = "  =>  ")
                current_ab = current_ab.abajo


        print('\n el tamano de la lista es ', self.size)
    
    def recorrer_fin(self):
        current = self.ultimo

        while current: # mientras que aux != None
            print('(',current.dato, ' x:' ,current.x, ' y:' ,current.y,')', end = "  =>  ")
            current = current.arriba
        print('\n el tamano de la lista es ', self.size)


