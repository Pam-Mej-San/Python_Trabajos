#Creamos un diccionario
persona= {
    'Nombre': 'Aurora',
    'Edad': 36,
    'Ciudad' : 'Colón - Entre Ríos'
}

#Usamos el método values
valores= persona.values()

#imprimimos

print('Valores del diccionario:', valores)

#Convertir valores en una lista

valores_lista= list(valores)
print('Valores como lista:', valores_lista)