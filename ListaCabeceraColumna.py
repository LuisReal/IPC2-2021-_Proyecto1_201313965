from NodoCabeceraColumna import NodoCabeceraColumna

class ListaCabeceraColumna:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nodo_nuevo_cabecera = None
    
    def vacia(self):
        return self.primero == None

    def insertar(self, x):
        self.nodo_nuevo_cabecera = NodoCabeceraColumna(x)
        
        if self.vacia():
            self.primero = self.ultimo = NodoCabeceraColumna(x)

        elif self.nodo_nuevo_cabecera.x < self.primero.x:
            self.agregar_inicio(x)
            self.nodo_nuevo_cabecera.columna # se inserta la lista vertical en la cabecera de las columnas

        elif self.nodo_nuevo_cabecera.x > self.ultimo.x:
            self.agregar_final(x)
            self.nodo_nuevo_cabecera.columna # se inserta la lista vertical en la cabecera de las columnas
        else:
            print('Hello World')
            #self.agregar_medio()
    
    def agregar_inicio(self, x):
        aux = NodoCabeceraColumna(x)
        self.primero.anterior = aux
        aux.siguiente = self.primero
        self.primero = aux
        

    def agregar_final(self,x):
        aux = NodoCabeceraColumna(x)
        self.ultimo.siguiente = aux
        aux.anterior = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        current = self.primero

        while current: # mientras que aux != None (mientras que el nodo no este vacio)
            #print(current.x, end = "  =>  ")
            current = current.siguiente

    def buscar(self, x):
        if not self.vacia():      
            temp = self.nodo_nuevo_cabecera
            temp = self.primero
            while (temp != None):
                if temp.x == x:
                    return print('La cabecera columna existe ',temp.x)
                
                temp = temp.siguiente
        return None