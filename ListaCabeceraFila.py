from NodoCabeceraFila import NodoCabeceraFila


class ListaCabeceraFila:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nodo_nuevo_cabecera = None

    def vacia(self):
        return self.primero == None

    def insertar(self, y):
        self.nodo_nuevo_cabecera = NodoCabeceraFila(y)
        

        if self.vacia():
            self.primero = self.ultimo = NodoCabeceraFila(y)

        elif self.nodo_nuevo_cabecera.y < self.primero.y:
            self.agregar_inicio(y)
            self.nodo_nuevo_cabecera.fila

        elif self.nodo_nuevo_cabecera.y > self.ultimo.y:
            self.agregar_final(y)
            self.nodo_nuevo_cabecera.fila
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
            #print(current.y, end = "  =>  ")
            current = current.siguiente

    def buscar(self, y):
        if not self.vacia():
            temp = self.nodo_nuevo_cabecera
            temp = self.primero
            while (temp != None):
                if temp.y == y:
                    return print('La cabecera fila existe ',temp.y)
                
                temp = temp.siguiente
        return None
            