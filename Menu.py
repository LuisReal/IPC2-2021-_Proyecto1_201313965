
from Archivo import Carga
from MatrizOrtogonal import MatrizOrtogonal

class Menu:

    def __init__(self):
        
        self.archivo = ""
        self.ruta = ""
        self.nombre_terreno = ""
        self.obj = ""
        self.obj_Lista = ""
        self.matriz = ""

    def menu(self): 

        opcion = 0
        
        while opcion != 6:
            print("\nMenu Principal: \n1.Cargar Archivo \n2.Procesar Archivo \n3.Escribir Archivo Salida" 
            "\n4.Mostrar datos del estudiante"
            "\n5.Generar Grafica"
            "\n6.Salida")

            opcion = int(input("Ingrese una opcion \n"))
            
            if opcion == 1:
                self.ruta = input("Ingrese la ruta del archivo: ")
                
                print("\nSe cargo la ruta del archivo exitosamente\n")

            elif opcion == 2:
                
                print("el archivo se esta procesando\n")
                
                
                self.nombre_terreno = input("Ingrese el nombre del terreno a procesar: ")
                self.obj = Carga()
                
                self.obj.archivo(self.ruta, self.nombre_terreno)
                
                
                
                
            elif opcion == 3:
                print("va a escribir el archivo\n")
                
            elif opcion == 4:
                print("Luis Fernando Gonzalez Real \n201313965 \nIntroduccion a la Programacion y Computacion 2 seccion E"
                "\nIngenieria en Ciencias y Sistemas \n4to Semestre \n")
                
            elif opcion == 5:
                print("mostrar grafica \n")
                
            elif opcion == 6:
                print("salio")  
                
            else:
                print("\nIngresa una opcion correcta \n") 

obj = Menu()
obj.menu()