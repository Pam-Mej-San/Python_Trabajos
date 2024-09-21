#Crear un diccionario
persona={
    'Nombre': 'Emilia',
    'Edad': 33,
    'Ciudad': 'CABA'
}

#Comprobar si una clave existe en el diccionario antes de acceder a su valor
clave='edad'


if clave in persona:
    valor= persona[clave]
    print(f'El valor de {clave}es:{valor}')
else:
    print(f'La clave {clave} no existe en el diccionario')

#Intentar acceder a una clave no existente

clave_inexistente='país'

if clave_inexistente in persona:
    valor=persona[clave_inexistente]
    print(f'El valor de {clave_inexistente} es: {valor}')
else:
    print(f'La calve {clave_inexistente} no existe en el diccionario.')

#Otra opción de comprobar

persona_2= {
    'Nombre': 'Emilia',
    'Edad': 33,
    'Ciudad': 'CABA'
}

print('Nombre' in persona_2)
