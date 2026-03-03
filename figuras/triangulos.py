from figuras.figura import Figura

class Triangulo(Figura): 
    
    def __init__(self): 
        super().__init__()
        self.base="" 
        self.altura="" 
        
    def leerDatosTriangulo(self): 
        self.base = float(input("Base:") )
        self.altura = float(input("Altura:") )
 
 
    def mostrarDatosTriangulo(self): 
        self.area = (self.base * self.altura) / 2
        print("Base:",self.altura)  
        print("Altura:",self.base)  
        print("Area:",self.area)