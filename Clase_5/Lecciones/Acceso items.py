#Crear un diccionrio
persona= {
    'Nombre': 'Alejandra',
    'Edad': 30,
    'Ciudad': 'Mérida'
}

#Usamos el método
pares_clave_valor= persona.items()

#Imprimimos
print('Pares clave valor:', pares_clave_valor)


#Convertir valores en una lista en pares con la 
#categoría correspondiente
valores_lista= list(pares_clave_valor)
print('Valores como lista:', valores_lista)

