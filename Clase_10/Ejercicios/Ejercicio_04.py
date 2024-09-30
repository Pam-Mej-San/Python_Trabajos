#Define una clase Producto con atributos como nombre, precio,
#y cantidad. Agrega métodos para aumentar o disminuir la
#cantidad de productos. Luego, crea una clase Inventario que
#contenga una lista de productos y métodos para agregar y
#mostrar productos.
#


# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre      # Atributo
        self.precio = precio      # Atributo
        self.cantidad = cantidad  # Atributo

    def aumentar_cantidad(self, cantidad):
        self.cantidad += cantidad  # Aumentamos productos

    def disminuir_cantidad(self, cantidad):
        if cantidad > self.cantidad:
            print(f'No se puede disminuir. Solo hay {self.cantidad} disponibles.')
        else:
            self.cantidad -= cantidad  # Disminuir productos

    def __str__(self):
        return f'Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}'

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos
    
    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agregar un nuevo producto a la lista

    def mostrar_productos(self):
        if not self.productos:  # Verificar si la lista está vacía
            return 'No hay productos en el inventario.'
        
        return [str(producto) for producto in self.productos]  # Mostrar los productos

# Ejemplo de uso
# Crear instancias de Producto
producto1 = Producto('Manzana', 0.5, 100)
producto2 = Producto('Plátano', 0.3, 150)
producto3 = Producto('Naranja', 0.8, 200)

# Crear instancia de Inventario
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar productos en el inventario
print('-'*40)
print(inventario.mostrar_productos())
print('-'*40)

# Aumentar la cantidad de un producto
producto1.aumentar_cantidad(50)
print('-'*40)

# Disminuir la cantidad de un producto
producto2.disminuir_cantidad(30)
print('-'*40)

# Mostrar productos en el inventario después de las modificaciones
print(inventario.mostrar_productos())
print('-'*40)

# Intentar disminuir más de la cantidad disponible
producto3.disminuir_cantidad(300)  # Debería dar un mensaje de error
print('-'*40)





