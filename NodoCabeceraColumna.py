from ListaVertical import Lista_V

class NodoCabeceraColumna:

    def __init__(self, x):
        self.x = x
        self.siguiente = None
        self.anterior = None
        self.columna = Lista_V()