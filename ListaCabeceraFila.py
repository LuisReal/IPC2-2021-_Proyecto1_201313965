from NodoCabeceraFila import NodoCabeceraFila


class ListaCabeceraFila:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def insertar(self, y):
        nodo_nuevo = NodoCabeceraFila(y)
        if self.vacia():
            self.primero = self.ultimo = NodoCabeceraFila(y)

        elif nodo_nuevo.y < self.primero.y:
            self.agregar_inicio(y)

        elif nodo_nuevo.y > self.ultimo.y:
            self.agregar_final(y)
        else:
            print('Hello World')
            #self.agregar_medio()
    
    def agregar_inicio(self, y):
        aux = NodoCabeceraFila(y)
        self.primero.anterior = aux
        aux.siguiente = self.primero
        self.primero = aux
        

    def agregar_final(self, y):
        aux = NodoCabeceraFila(y)
        self.ultimo.siguiente = aux
        aux.anterior = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        current = self.primero

        while current: # mientras que aux != None (mientras que el nodo no este vacio)
            print(current.y, end = "  =>  ")
            current = current.siguiente

    def buscar(self, y):
        if not self.vacia():
            aux = NodoCabeceraFila(y)
            temp = self.primero
            while (temp != None):
                if temp.y == y:
                    return print('La cabecera existe ',temp.y)
                
                temp = temp.siguiente
        print('La cabecera no existe')
            