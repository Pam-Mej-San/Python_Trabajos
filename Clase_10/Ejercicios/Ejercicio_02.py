#Define una clase base Forma con un método area().

#Super:
class Forma:
    def __init__(self,nombre):
        self.nombre=nombre

    def area(self):
        return NotImplementedError('Mejor ve a las subclases')
        
#Luego, crea subclases Rectangulo, Circulo, y Triangulo que 
#implementen el método area() de manera específica
#Subclases:
class Rectángulo(Forma):
    def __init__(self, base, altura):
        super().__init__('Rectángulo') # Llama al constructor de  Forma
        self.base=base #para convocar a los datos de base según su formula
        self.altura=altura #para convocar a los datos de altura según su formula
    
    def area(self):
        return self.base * self.altura #Función basado en fórmula
    
#Clase Triángulo

class Triángulo(Forma):
    def __init__(self, base, altura):
        super().__init__('Triángulo')  # Llama al constructor de  Forma
        self.base=base #para convocar a los datos de base según su formula
        self.altura=altura #para convocar a los datos de altura según su formula
    
    def area(self):
        return (self.base * self.altura)/2 #Fórmula para el triángulo

#Clase círculo
class Círculo(Forma):
    def __init__(self, radio):
        super().__init__("Círculo")  # Llama al constructor de Forma
        self.radio = radio #para convocar a los datos de radio según su formula
    

    def area(self):
        return (3.1416) * (self.radio ** 2)

#Usa polimorfismo para crear una lista de formas y calcular el área
#de cada una
formas = [
    Rectángulo(8, 3),
    Círculo(30),
    Triángulo(4, 13)
]

#Calculando..... e imprimiendo..
for forma in formas:
    print(f"{forma.nombre} - Área: {forma.area()}")