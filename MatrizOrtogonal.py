from IPC2_Proyecto1_201313965.NodoCabeceraColumna import NodoCabeceraColumna
from ListaCabeceraFila import ListaCabeceraFila
from ListaCabeceraColumna import ListaCabeceraColumna
from NodoOrtogonal import Nodo


class MatrizOrtogonal:

    def __init__(self):
        self.lista_fila = ListaCabeceraFila()
        self.lista_columna = ListaCabeceraColumna()

    def insertar(self, dato, x, y):
        aux = Nodo(dato, x, y)

        if self.lista_columna.buscar(x) == None:
            self.lista_columna.insertar(x)
        if self.lista_fila.buscar(y) == None:
            self.lista_fila.insertar(y)
