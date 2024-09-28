class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicializa el atributo 'nombre' del animal

    def hacer_sonido(self):
        return "Sonido de animal"  # Método genérico que puede ser sobreescrito

# Ahora, puedes crear subclases como Perro y Gato, que heredan de Animal:

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"  # Sobrescribe el método para el sonido específico de un perro

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"  # Sobrescribe el método para el sonido específico de un gato

mi_perro = Perro("Rex")
mi_gato = Gato("Miau")

print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")

