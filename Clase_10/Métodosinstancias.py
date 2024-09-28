# Métodos de instancias

#Definimos la clase 

class Perro:
    def __init__(self, raza, nombre):
        self.raza= raza #atributo de instancia
        self.nombre= nombre #Atributo de instancia

#Método para mostrar información del perrito

    def mostrar_info(self):
        return f'Perro: {self.raza}{self.nombre}'

#Crear un objeto de la clase perro

mi_perro= Perro('Mestiza ','Canelita')

#Usar el método de objeto

print(mi_perro.mostrar_info())

#En la clase Perro el método mostrar_info es un método de instancia que proporciona
# una representación de la información del perro al acceder a sus atributos
# Este método permite realizar acciones específicas sobre los datos del objeto como tal
#Y se invoca a través de la instancia de Perro para obtener la información de ese perro en particular

