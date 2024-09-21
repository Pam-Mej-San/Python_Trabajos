#Ejemplo de diccionario
diccionario_vacío={}
print('Ejemplo de un diccionario vacío', diccionario_vacío)

#Ejemplo básico de un diccionario
persona={
    'Nombre': 'María',
    'Edad': 30,
    'Casada': False,
    'Hijos': ['Ana', 'Luis'],
    'Dirección':
        { 
            'Calle': 'La gran vía',
            'Ciudad': 'Madrid'
        }
}

print('Ejemplo de diccionario simple', persona)

#Ejemplo de diccionario mixto
diccionario_mixto= {
        'Nombre': 'Alejandra',
        1:[2,3,4],
        (2,3): 'Tupla como clave' #Tupla es una clave y valor es un string
}

print('Ejemplo de diccionario mixto', diccionario_mixto)