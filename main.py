from figuras.figura import Figura
from figuras.circulos import Circulo
from figuras.triangulos import Triangulo

def main():

    cir = Circulo() 
    cir.leerDatosCirculo() 
    cir.leerDatosFigura() 
    cir.mostrarDatosCirculo() 
    cir.mostrarDatosFigura()
    print("********************") 
    tri = Triangulo()
    tri.leerDatosTriangulo() 
    tri.leerDatosFigura()   
    tri.mostrarDatosTriangulo() 
    tri.mostrarDatosFigura()
    
    
if __name__ == "__main__":
    main()