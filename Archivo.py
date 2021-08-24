import xml.etree.ElementTree as ET


class Carga:
    def __init__(self):
        self.doc = ""
        self.fila = 0
        self.columna = 0
        self.nombre_terreno = ""
        
   
    def archivo(self, ruta, nombre):
    
        xmlfile = ruta
        self.nombre_terreno = nombre

        doc = ET.parse(xmlfile)
        root = doc.getroot()

        #print(root[0][3].attrib)

        ''' for position in root.iter('posicion'): 
            print(position.attrib,'  ', position.text) 
            
        '''   

        for elemento in root.findall('terreno'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            if elemento.get('nombre') == self.nombre_terreno: # se compara el nombre del terreno que se ingresa con el del archivo xml
                m = elemento.find('./dimension/m').text #se busca el valor de dimension m solamente para el terreno ingresado
                print('\n el valor de dimension m (fila) es ', m)

                n = elemento.find('./dimension/n').text
                print('\n el valor de dimension n (columna) es ', n)

                posicion_inicio_x = elemento.find('./posicioninicio/x').text
                print('\n el valor de posicioninicio en x es ', posicion_inicio_x)

                posicion_inicio_y = elemento.find('./posicioninicio/y').text
                print('\n el valor de posicioninicio en y es ', posicion_inicio_y)

                posicion_fin_x = elemento.find('./posicionfin/x').text
                print('\n el valor de posicionfin en x es ', posicion_fin_x)

                posicion_fin_y = elemento.find('./posicionfin/y').text
                print('\n el valor de posicionfin en y es ', posicion_fin_y)

            


        
'''
        for dimension_columna in root.findall("./terreno[@nombre='self.nombre_terreno']/dimension/n"):
            n = dimension_columna.text
            print('el valor de dimension n (columna) es ',n)

        for posicion_inicio_x in root.findall('./terreno/posicioninicio/x'):
            x = posicion_inicio_x.text
            print('el valor de la posicion inicio en x es ',x)

        for posicion_inicio_y in root.findall('./terreno/posicioninicio/y'):
            y = posicion_inicio_y.text
            print('el valor de la posicion inicio en y es ',y)

        for posicion_fin_x in root.findall('./terreno/posicionfin/x'):
            x = posicion_fin_x.text
            print('el valor de la posicion fin en x es ',x)

        for posicion_fin_y in root.findall('./terreno/posicionfin/y'):
            y = posicion_fin_y.text
            print('el valor de la posicion fin en y es ',y)
'''
            
''' 
            self.fila = int(matriz_prueba.get('n'))
            self.columna = matriz_prueba.get('m')

            print("\nel nombre de la matriz es: ", nombre, "\nel numero de filas es: ", self.fila,
            "\nel numero de columnas es: ", self.columna)
            print("el tamano de la matriz es: ", len(matriz_prueba),"\n") 
'''