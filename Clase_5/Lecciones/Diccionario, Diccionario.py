# Crear un diccionario que represente a una persona
persona= {
    'Nombre': 'Ana',
    'Edad': 30,
    'Dirección': {
        'Calle':'Gran Vía',
        'Ciudad': 'Madrid',
        'Código_Postal': 28013
    }
}
#Acceder a los elementos del diccionario anidado
#Imprimir a la ciudad de la dirección

print('Ciudad:', persona ['Dirección']['Ciudad']) #Output : Madrid

#Acceder a la callde dentro del diccionario anidado.
print('Calle:', persona ['Dirección']['Calle'])  #Output: Gran Vía

#Acceder al código postal dentro del diccionario anidado.
print('Código Postal:', persona['Dirección']['Código_Postal']) #Output: 28013

