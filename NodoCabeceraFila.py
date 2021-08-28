from ListaHorizontal import Lista_H

class NodoCabeceraFila:

    def __init__(self, y):
        self.y = y
        self.siguiente = None
        self.anterior = None
        self.fila = Lista_H()