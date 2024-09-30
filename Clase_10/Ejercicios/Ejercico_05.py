#
#Clases de Vehículos
#o Crea una clase base Vehiculo que tenga atributos marca y
#modelo. Luego, crea subclases Coche y Motocicleta que
#hereden de Vehiculo. Implementa el método mostrar_info() en
#cada subclase que utilice super() para mostrar la información
#básica y luego la específica de cada vehículo.
#
#  Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo
        self.modelo = modelo    # Atributo

    def mostrar_info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'

# Subclase Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)  # Llamar al constructor de la clase base
        self.numero_puertas = numero_puertas  # Atributo específico de Coche

    def mostrar_info(self):
        info_basica = super().mostrar_info()  # Obtener la información básica
        return f'{info_basica}, Número de Puertas: {self.numero_puertas}'

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llamar al constructor de la clase base
        self.tipo = tipo  # Atributo específico de Motocicleta

    def mostrar_info(self):
        info_basica = super().mostrar_info()  # Obtener la información básica
        return f'{info_basica}, Tipo: {self.tipo}'

# Ejemplo de uso
# Crear instancias de Coche y Motocicleta
coche = Coche('Meteoro', 'MAC 5', 4)
motocicleta = Motocicleta('Yamaha', 'QR', 'Deportivo')

# Mostrar información de cada vehículo
print('-'*40)
print(coche.mostrar_info())           # Salida: Marca: Meteoro, Modelo: MAC 5, Número de Puertas: 4
print('-'*40)
print(motocicleta.mostrar_info())     # Salida: Marca: Yamaha, Modelo:QR, Tipo: Deportiva
print('-'*40)
