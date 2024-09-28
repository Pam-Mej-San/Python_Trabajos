# Atributos de instancia

#Definimos la clase 

class Gato:
    def __init__ (self, color, nombre):
        self.color= color #Atributo de la instancia
        self.nombre = nombre #atributo instancia
    
#Crear diferentes bjetos (instancias) de la clase gato

gato1 = Gato('Negro', 'Félix')
gato2 = Gato('Naranja', 'Garfield')

#Acceder a los atributos de instancia

print(gato1.color)
print(gato2.color)

#La clase de Gato incluye atributos de la insntancia, color y nombre que se inicializan en el constructor
# Cada objeto creado a partir de esta clase (como gato 1 y gato 2 ) tiene sus propios valotes
# para estos atributos
# Lo que permite que diferentes instancias representen gatos distintos con características únicas

