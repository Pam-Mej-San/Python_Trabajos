# Crear un diccionario
persona= {
    'Nombre': 'Emilia',
    'Edad': 33,
    'Ciudad': 'CABA',
    'Profesión': 'Veterinaria'
}

#Imprimir el diciconario original
print('Diccionario original:',persona)

#Usamos popItem para eliminar y obtener el último par 
#clave-valor 

ultimo_elemento=persona.popitem ()

#Imprimimos el par clave-valor
print('Último par clave-valor eliminado:', ultimo_elemento)

#Imprimimos después de usar PopItem
print('Diccionario después de usar PopItem', persona)


