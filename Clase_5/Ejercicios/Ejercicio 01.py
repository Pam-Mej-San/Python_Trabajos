#Crear y Acceder a un Diccionario Básico
#1. Crea un diccionario que contenga la siguiente información sobre un
#libro:
#o Título
#o Autor
#o Año de publicación
#o Género
#2. Accede e imprime cada uno de estos valores usando las claves
#correspondientes.

detalles_libro= {

     'Título':'Norte y Sur',
     'Autor':'Elizabeth Gaskell',
     'Año de publicación':1855,
     'Género': 'Novela Social'
}

valores=detalles_libro.values()
print('Detalles del libro:', valores, '\n')

valoresenlista=list(valores)
print('Valores como lista:',valoresenlista,'\n')


