#Modificar un Valor en un Diccionario Anidado
#1. Crea un diccionario que contenga información sobre una tienda de
#libros, con las siguientes claves:
#o nombre_tienda
#o libros, que es una lista de diccionarios, donde cada diccionario
#representa un libro con claves titulo y precio.
#2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99)

nombre_tienda= {
    'Nombre':'Alejandría',
    'Libros':[
    {'Título':'Orgullo y Prejuicio', 'Precio': 210},
    {'Título':'Farenheit 451', 'Precio': 200},
    {'Título':'Frankenstein', 'Precio': 250},
    {'Título':'La Iliada', 'Precio': 110}
    ]
}
nombre_tienda['Libros'][1]['Precio']= 15.99
print('\n',nombre_tienda,'\n')
print()

print('Libros disponibles en stock\n')
for libro in nombre_tienda['Libros']:
    print("Título:", libro['Título'])
    print("Precio:", libro['Precio'])
    print()
