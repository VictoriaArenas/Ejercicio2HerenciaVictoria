import math 
from figuras.figura import Figura

class Circulo(Figura): 
    
    def __init__(self): 
        super().__init__()
        self.radio="" 
        
    def leerDatosCirculo(self): 
        self.radio = float(input("Radio:") )
 
    def mostrarDatosCirculo(self): 
        self.area = ( math.pi * (self.radio * self.radio) )
        print("El radio es de :",(self.radio))  
        print("El area es de :",(self.area))  
        