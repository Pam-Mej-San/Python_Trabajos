# Métodos de clase

#Definimos una clase

class Conejo:
    cantidad_conejos=0 #Atributo de clase
    
    def __init__(self, color, nombre):
        self.color=color #Atributo de instancia.
        self.nombre=nombre #Atributo de instancia
        Conejo.cantidad_conejos+=1 #Aumenta la cantidad total de conejos
    #Método de clase para obtener el total de conejos 
    @classmethod
    def total_conejos(cls):
        return f'Total de conejos: {cls.cantidad_conejos}'
    
#Crear instancias de la clase conejo

Conejo1=Conejo('Gris', 'Tambor')
Conejo2=Conejo('Blanco', 'Pochoclo')

# Llamas al método de clase

print(Conejo.total_conejos())

#La clase conejo incluye un método de clase total_conejos que se utiliza para acceder 
# a un atributo de clase(cantidad_conejos)
#Este método permite realizar operaciones que afectan a la clase en su totalidad
#en lugar de a instancias individuales
#Lo que facilita el seguimiento de cuantos objetos de esa clase han sido creados
