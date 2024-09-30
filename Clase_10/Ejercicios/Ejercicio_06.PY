#Crea una clase Libro con atributos titulo, autor, y paginas.
#Luego, crea una clase Biblioteca que contenga una lista de
#libros. Agrega métodos para añadir libros, buscar por autor y
#mostrar todos los libros. Implementa encapsulamiento para
#proteger la lista de libros.
#
#

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo      # Atributo
        self.autor = autor        # Atributo
        self.paginas = paginas    # Atributo

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}'

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.__libros = []  # Lista de libros, protegida por encapsulamiento

    def añadir_libro(self, libro):
        self.__libros.append(libro)  # Añadir un libro a la lista

    def buscar_por_autor(self, autor):
        return [libro for libro in self.__libros if libro.autor == autor]  # Buscar libros por autor

    def mostrar_libros(self):
        if not self.__libros:  # Verificar si la lista está vacía
            return 'No hay libros en la biblioteca.'
        
        return [str(libro) for libro in self.__libros]  # Mostrar todos los libros

# Ejemplo de uso
# Crear instancias de Libro
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 400)
libro2 = Libro('Orgullo y Prejuicio', 'Jane Austen', 360)
libro3 = Libro('1984', 'George Orwell', 328)
libro4 = Libro ('Farenheit 451', 'Ray Bradbury', 272)

# Crear instancia de Biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.añadir_libro(libro4)


# Mostrar todos los libros
print('-'*40)
print('Libros en la biblioteca:')
print('-'*40)
print(biblioteca.mostrar_libros())

# Buscar libros por autor
print('-'*40)
print('\nLibros de Gabriel García Márquez:')
for libro in biblioteca.buscar_por_autor('Gabriel García Márquez'):
    print(libro)
print('-'*40)