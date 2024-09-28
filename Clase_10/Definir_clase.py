#1. Definir una Clase en python 

#Definimos una clase llamada coche

class Coche:
    #Método __init__ es el constructor que se llama al crear un nuevo objeto
    def __init__(self, marca, modelo):
    # Self es una referencia al objeto que estamos creando
    # inicializamos los atributos de la instancia.}
        self.marca =marca #Atributo de instancia que guarda la marca
        self.modelo =modelo #Atributo de instancia que guarda la marca

#La clase coche es una plantilla para crear objetos de tipo auto
#Contiene un método constructor __init__ que inicializa los atributos específicos de cada coche que
#hagamos
#Como por ejemplo: marca, modelo usando la referencia self para
#distinguir entre las propiedades del objeto y los parámetros pasados al constructor



        