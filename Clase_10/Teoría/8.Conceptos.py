class Animal:  # Superclase
    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):  # Subclase
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):  # Subclase
    def hacer_sonido(self):
        return "Miau"
    
# Crear instancias
mi_perro = Perro()
mi_gato = Gato()

# Llamar al método y mostrar los sonidos
print(f"El perro dice: {mi_perro.hacer_sonido()}")
print(f"El gato dice: {mi_gato.hacer_sonido()}")