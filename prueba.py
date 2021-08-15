import xml.etree.ElementTree as ET


class Carga:
    def __init__(self):
        self.doc = ""
        self.fila = 0
        self.columna = 0
        self.matriz = []
        self.diccionario = {}
   
    def archivo(self, ruta):
    
        xmlfile = ruta

        doc = ET.parse(xmlfile)
        root = doc.getroot()

        #print(root[0][3].attrib)

        for position in root.iter('posicion'): 
            print(position.attrib)
             

        for matriz_prueba in root.findall('terreno'): # terreno es el nombre de la etiqueta del archivo robot.xml
            nombre = matriz_prueba.get('nombre') # nombre es la etiqueta adentro de la etiqueta terreno
            print(nombre)
''' 
            self.fila = int(matriz_prueba.get('n'))
            self.columna = matriz_prueba.get('m')

            print("\nel nombre de la matriz es: ", nombre, "\nel numero de filas es: ", self.fila,
            "\nel numero de columnas es: ", self.columna)
            print("el tamano de la matriz es: ", len(matriz_prueba),"\n") 
'''