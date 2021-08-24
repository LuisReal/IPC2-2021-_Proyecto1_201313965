import xml.etree.ElementTree as ET


class Carga:
    def __init__(self):
        self.doc = ""
        self.fila = 0
        self.columna = 0
        
   
    def archivo(self, ruta):
    
        xmlfile = ruta

        doc = ET.parse(xmlfile)
        root = doc.getroot()

        #print(root[0][3].attrib)

        for position in root.iter('posicion'): 
            print(position.attrib,'  ', position.text)
            
             

        for elemento in root.findall('terreno'): # terreno es el nombre de la etiqueta del archivo robot.xml
            nombre = elemento.get('nombre') # nombre es la etiqueta adentro de la etiqueta terreno
            
            print('\n',nombre)

        for dimension_fila in root.findall('./terreno/dimension/m'):
            m = dimension_fila.text
            print('el valor de dimension m (fila) es ',m)

        for dimension_columna in root.findall('./terreno/dimension/n'):
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
            self.fila = int(matriz_prueba.get('n'))
            self.columna = matriz_prueba.get('m')

            print("\nel nombre de la matriz es: ", nombre, "\nel numero de filas es: ", self.fila,
            "\nel numero de columnas es: ", self.columna)
            print("el tamano de la matriz es: ", len(matriz_prueba),"\n") 
'''