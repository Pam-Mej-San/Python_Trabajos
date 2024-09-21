#1. Crea un diccionario que represente una clase con los siguientes
#datos:
#o nombre_clase
#o estudiantes, que es una lista de diccionarios con información
#de cada estudiante (nombre y edad).
#2. Escribe una función que busque la edad de un estudiante dado su
#nombre usando el índice de la lista en lugar de bucles (suponiendo
#que conoces el índice).
#3. Imprime la edad del estudiante buscado.

Clase= {
    'Clase': 'Navegación en altamar',
    'Lista de Estudiantes':[
    {'Nombre': 'Luisa', 'Edad': 25},
    {'Nombre': 'Clark', 'Edad': 28},
    {'Nombre': 'Jimmy', 'Edad': 22}
    ]
}

índices= {
    'Luisa':0,
    'Clark':1,
    'Jimmy':2,
}

def edad_por_nombre(nombre):
    if nombre in índices:
        índice= índices[nombre]
        edad= Clase['Lista de Estudiantes'][índice]['Edad']
        print(f'La edad del estudiante {nombre} es: {edad}')
    else:
        print('No encontrado')

búsqueda_nom=input('Ingresa el nombre de la persona que buscas:')
edad_por_nombre(búsqueda_nom)
