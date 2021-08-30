from NodoCabeceraColumna import NodoCabeceraColumna

class ListaCabeceraColumna:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nodo_nuevo_cabecera = None
    
    def vacia(self):
        return self.primero == None

    def insertar(self, dato, x, y):
        
        # ListaCabeceraColumna().buscar(se obtiene el NodoCabeceraColumna) 
        # En el NodoCabeceraColumna insertamos la listaVertical y en la lista vertical insertamos un NodoOrtogonal
        self.nodo_nuevo_cabecera = NodoCabeceraColumna(dato, x, y)
        
        if self.vacia():
            self.primero = self.ultimo = self.nodo_nuevo_cabecera

        elif self.nodo_nuevo_cabecera.x < self.primero.x:
            self.agregar_inicio(dato, x, y)
             

        elif self.nodo_nuevo_cabecera.x > self.ultimo.x:
            self.agregar_final(dato, x, y)
            
        #else:
            #print('Hello World')
            #self.agregar_medio()
    
    def agregar_inicio(self, dato, x, y):
        aux = NodoCabeceraColumna(dato, x, y)
        self.primero.anterior = aux
        aux.siguiente = self.primero
        self.primero = aux
        

    def agregar_final(self, dato, x, y):
        aux = NodoCabeceraColumna(dato, x, y)
        self.ultimo.siguiente = aux
        aux.anterior = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        current = self.primero

        while current: # mientras que aux != None (mientras que el nodo no este vacio)
            #print(current.x, end = "  =>  ")
            current = current.siguiente

    def buscar(self, x):
        if not self.vacia(): # si no esta vacia      
            #temp = self.nodo_nuevo_cabecera #NodoCabeceraColumna(dato, x, y)
            temp = self.primero
            while (temp is not None):
                if temp.x == x:
                    return temp
                
                temp = temp.siguiente
        else:
            return None