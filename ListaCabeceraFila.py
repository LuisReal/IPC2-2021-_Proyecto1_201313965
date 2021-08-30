from NodoCabeceraFila import NodoCabeceraFila


class ListaCabeceraFila:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nodo_nuevo_cabecera = None

    def vacia(self):
        return self.primero == None # retorno True o False

    def insertar(self, dato, x, y):
        nodo_nuevo_cabecera = NodoCabeceraFila(dato, x, y)
        

        if self.vacia():
            self.primero = self.ultimo = nodo_nuevo_cabecera

        else: 
            if self.nodo_nuevo_cabecera.y < self.primero.y:
                self.agregar_inicio(dato, x, y)
            

            elif self.nodo_nuevo_cabecera.y > self.ultimo.y:
                self.agregar_final(dato, x, y)
            
        #else:
            #print('Hello World')
            #self.agregar_medio()
    
    def agregar_inicio(self, dato, x, y ):
        aux = NodoCabeceraFila(dato, x, y )
        self.primero.anterior = aux
        aux.siguiente = self.primero
        self.primero = aux
        

    def agregar_final(self, dato, x, y):
        aux = NodoCabeceraFila(dato, x, y)
        self.ultimo.siguiente = aux
        aux.anterior = self.ultimo
        self.ultimo = aux
       

    def recorrer_inicio(self):
        
        if not self.vacia():
            tmp = self.primero

            while tmp is not None: # mientras que aux != None (mientras que el nodo no este vacio)
                print('dato: ',tmp.dato, '(x,y)',tmp.x,',', tmp.y)
                tmp = tmp.siguiente

    def buscar(self, y):
        if not self.vacia():
            
            temp = self.primero
            while (temp is not None):
                if temp.y == y:
                    return temp
                
                temp = temp.siguiente
        else:
            return None
            