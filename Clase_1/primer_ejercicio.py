Edad=28
nombre='Alejandra'
estudia= True

PI=3.14
País='México'

edad= input('Introduce tu edad:' )
nombre=input('introduce tu nombre:')

estudia= input ('¿Estás estudiando? Sí/No:').lower()=='Si'

cantidad_libros=10
titulo_libro='El principito'
es_interesante= True
temas=['Aventura', 'Fantasía', 'Filosofía']
autor= {
    'nombre': 'Antoine de Saint-Exupéry',
    'nacionalidad': 'Francesa'
}

edad_str= str(edad)
cantidad_libros_float= float(cantidad_libros)

print('Nombre', nombre)
print('Edad:', edad)
print('¿Estás estudiando?', estudia)
print('Constante Pi', PI)
print('Constante País', País)
print('Cantidad de libros', cantidad_libros)
print('Título de Libro', titulo_libro)
print('¿Es intereasante?',es_interesante)
print('Temas del libro',temas)
print('Autor del libro', autor)
print('Edad (como cadena de texto):',edad_str)
print('Cantidad de libros(como float)', cantidad_libros_float)

