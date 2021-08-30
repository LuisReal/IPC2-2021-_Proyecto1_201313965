from ListaHorizontal import Lista_H

class NodoCabeceraFila:

    def __init__(self, dato, x, y):
        self.dato = dato
        self.x = x
        self.y = y
        self.siguiente = None
        self.anterior = None
        Lista_H().insertar(dato, x, y)
        self.fila = Lista_H()