from xml.dom import minidom

class Carga:
    def __init__(self):
        self.doc = ""
    def archivo(self, ruta):
        self.doc = minidom.parse(ruta) #se ingresa la ruta completa del archivo para que funcione
