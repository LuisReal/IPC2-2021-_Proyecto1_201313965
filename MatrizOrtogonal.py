from NodoCabeceraColumna import NodoCabeceraColumna
from NodoCabeceraFila import NodoCabeceraFila
from ListaCabeceraFila import ListaCabeceraFila
from ListaCabeceraColumna import ListaCabeceraColumna
from NodoOrtogonal import Nodo


class MatrizOrtogonal:

    def __init__(self):
        self.lista_fila = ListaCabeceraFila()
        self.lista_columna = ListaCabeceraColumna()

    def insertar(self, dato, x, y):
        

        if self.lista_columna.buscar(x) is None: # si el NodoCabeceraCOlumna esta vacio
            self.lista_columna.insertar(dato, x, y) 
            
        if self.lista_fila.buscar(y) is None:
            self.lista_fila.insertar(dato, x, y)

        # tenemos que inserta un nodoOrtogonal en la lista vertical y la lista la insertamos en el NodoCabeceraColumna
        print('se inserto ', dato, ' en la posicion ',x,',',y)

    def llenar(self, x, y):
        self.x = x
        self.y = y
        dato = 1
        
        for a in range (self.x) :
            for b in range (self.y) :
                self.insertar(dato, a+1, b+1)
                dato += 1
                    

