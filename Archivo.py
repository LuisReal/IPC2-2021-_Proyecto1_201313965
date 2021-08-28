import xml.etree.ElementTree as ET
from ListaVertical import Lista

class Carga:
    def __init__(self):
        self.doc = ""
        self.fila = 0
        self.columna = 0
        self.nombre_terreno = ""
        self.n = 0
        self.m = 0
        self.obj = ""
        
   
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

                self.obj = Lista() # se tiene que agregar afuera del For para que imprima la lista correctamente
                contador_fila = 1
                contador_columna = 1
                for posicion in elemento.findall('posicion'): #se usa elemento.findall para recorrer etiqueta posicion de ese elemento = terreno ingresado     
                    if int(posicion.get('x')) == 1 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        print('\n El valor de x es ',x ,' El valor de y es ',y)
                        print('\n El valor de la posicion es ', dato)
                                
                        self.obj.agregar_final(dato, x, y)     
                        #print('\n La suma del valor de x es ', suma)
                    elif int(posicion.get('x')) == 2 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        print('\n El valor de x es ',x ,' El valor de y es ',y)
                        print('\n El valor de la posicion es ', dato)
                                
                        self.obj.agregar_final(dato, x, y)
                    
                    elif int(posicion.get('x')) == 3 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        print('\n El valor de x es ',x ,' El valor de y es ',y)
                        print('\n El valor de la posicion es ', dato)
                                
                        self.obj.agregar_final(dato, x, y)

                    elif int(posicion.get('x')) == 4 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        print('\n El valor de x es ',x ,' El valor de y es ',y)
                        print('\n El valor de la posicion es ', dato)
                                
                        self.obj.agregar_final(dato, x, y)

                    elif int(posicion.get('x')) == 5 :
                        
                        x = int(posicion.get('x'))
                        y = int(posicion.get('y'))
                        dato = posicion.text
                        print('\n El valor de x es ',x ,' El valor de y es ',y)
                        print('\n El valor de la posicion es ', dato)
                                
                        self.obj.agregar_final(dato, x, y)
                self.obj.recorrer_inicio()     

            else:
                print('\nEl nombre del terreno ingresado no existe ')
        
        #self.obj.recorrer_inicio()
        
        


            


        
