from ListaVertical import Lista_V

class NodoCabeceraColumna:

    def __init__(self, dato, x, y):
        self.dato = dato
        self.x = x
        self.y = y
        self.siguiente = None
        self.anterior = None
        Lista_V().insertar(dato, x, y) # se inserta la lista vertical en el NodoCabeceraColumna
        self.columna = Lista_V()