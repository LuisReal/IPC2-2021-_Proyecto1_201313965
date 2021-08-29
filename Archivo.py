from ListaCabeceraColumna import ListaCabeceraColumna
import xml.etree.ElementTree as ET
from ListaVertical import Lista_V
from ListaHorizontal import Lista_H
from ListaCabeceraFila import ListaCabeceraFila
from MatrizOrtogonal import MatrizOrtogonal

class Carga:
    def __init__(self):
        self.doc = ""
        self.fila = 0
        self.columna = 0
        self.nombre_terreno = ""
        self.n = 0
        self.m = 0
        self.obj_v = ""
        self.obj_h = ""
        self.obj_cabecera_fila = ""
        self.obj_cabecera_columna = ""
        self.obj_ortogonal = ""
        
   
    def archivo(self, ruta, nombre):
    
        xmlfile = ruta
        self.nombre_terreno = nombre

        doc = ET.parse(xmlfile)
        root = doc.getroot()


        for elemento in root.findall('terreno'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            if elemento.get('nombre') == self.nombre_terreno: # se compara el nombre del terreno que se ingresa con el del archivo xml
                self.n = int(elemento.find('./dimension/n').text)
                print('\n el valor de dimension n (fila) es ', self.n)

                self.m = int(elemento.find('./dimension/m').text) #se busca el valor de dimension m solamente para el terreno ingresado
                print('\n el valor de dimension m (columna) es ', self.m)

                posicion_inicio_x = elemento.find('./posicioninicio/x').text
                print('\n el valor de posicioninicio en x es ', posicion_inicio_x)

                posicion_inicio_y = elemento.find('./posicioninicio/y').text
                print('\n el valor de posicioninicio en y es ', posicion_inicio_y)

                posicion_fin_x = elemento.find('./posicionfin/x').text
                print('\n el valor de posicionfin en x es ', posicion_fin_x)

                posicion_fin_y = elemento.find('./posicionfin/y').text
                print('\n el valor de posicionfin en y es ', posicion_fin_y)

                self.obj_v = Lista_V() # se tiene que agregar afuera del For para que imprima la lista correctamente
                self.obj_h = Lista_H()
                self.obj_cabecera_fila = ListaCabeceraFila()
                self.obj_cabecera_columna = ListaCabeceraColumna()
                self.obj_ortogonal = MatrizOrtogonal()
                contador_fila = 1
                contador_columna = 1
                for posicion in elemento.findall('posicion'): #se usa elemento.findall para recorrer etiqueta posicion de ese elemento = terreno ingresado     
                    if int(posicion.get('x')) == 1 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        #print('\n El valor de x es ',x ,' El valor de y es ',y)
                        #print('\n El valor de la posicion es ', dato)

                        #self.obj_ortogonal.llenar(x, y)
                
                               
                        self.obj_v.insertar(dato, x, y) 
                        self.obj_h.insertar(dato, x, y) 
                        self.obj_cabecera_fila.insertar(y)
                        self.obj_cabecera_columna.insertar(x)   
                        #print('\n La suma del valor de x es ', suma)
                
                    elif int(posicion.get('y')) == 1 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        #print('\n El valor de x es ',x ,' El valor de y es ',y)
                        #print('\n El valor de la posicion es ', dato)
                                
                        self.obj_v.insertar(dato, x, y) 
                        self.obj_h.insertar(dato, x, y) 
                        self.obj_cabecera_fila.insertar(y)
                        self.obj_cabecera_columna.insertar(x)
                    
                    
                self.obj_v.recorrer_inicio()
                self.obj_h.recorrer_inicio()
                self.obj_cabecera_fila.recorrer_inicio()
                self.obj_cabecera_fila.buscar(5)
                self.obj_cabecera_columna.recorrer_inicio()
                self.obj_cabecera_columna.buscar(5)  
                    

            #else:
                #print('\nEl nombre del terreno ingresado no existe ')
        
        #self.obj.recorrer_inicio()
        
        


            


        
