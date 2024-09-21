#Crear un diccionario con información de una persona
persona={
    'nombre': 'Catalina',
    'edad': 33,
    'ciudad' : 'Bogotá'

}

# Acceder a los elementos usando corchetes

nombre= persona ['nombre']
edad= persona ['edad']
ciudad= persona ['ciudad']

#imprimir valores

print('Nombre:', nombre)
print('Edad:', edad)
print('Ciudad:', ciudad)

#Intentar acceder a una clave que no existe
#print(persona [país])