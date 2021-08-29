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
        nodo_nuevo = Nodo(dato, x, y)

        if self.lista_columna.buscar(x) is None:
            self.lista_columna.insertar(x)
        if self.lista_fila.buscar(y) is None:
            self.lista_fila.insertar(y)

    
        print('se inserto ', dato, ' en la posicion ',x,' ',y, end = ' => ')

    def llenar(self, dato, x, y):
        self.x = x
        self.y = y
        
        for y in range (self.y) :
            for x in range (self.x) :
                self.insertar(dato, x, y)
                

