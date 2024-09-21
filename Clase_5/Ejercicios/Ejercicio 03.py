#Crea un diccionario que represente una persona con las siguientes
#claves:
#o Nombre
#o Edad
#o Dirección (donde la dirección es otro diccionario con claves:
#Calle, Ciudad, Código postal)
#2. Imprime la ciudad de la dirección.

persona= {
    'Nombre':'Pamela',
    'Edad':28,
    'Dirección': {
        'Calle': 12,
        'Ciudad':'Jaramillo',
        'Código Postal': 8902
    }
}

print('\nCiudad', persona ['Dirección']['Ciudad'],'\n')
