# Crear tupla con varios valores

tupla_mixta= (1, 'Hola', 3.5)

# Mostrar completa la tupla
print( 'Tupla completa:', tupla_mixta)

#Acceder a los elementos de la tupla por su índice (posición)
print('Primer elemento de la tupla', tupla_mixta[0])
print('Segundo elemento de la tupla', tupla_mixta[1])
print('Tercer elemento de la tupla', tupla_mixta[2])

#Explicación de tuplas inmutables
print('\n Las tuplas no se pueden modificar. Intentemos cambiar el primer elemento')

#Ejemplo de cambio que causaría un error
#tupla_mixta[0]=10

#Explicación clara de la inmutabilidad (inmortalidad)

print("Si intentamos hacer 'tupla_mixta[0]=10', Python mostrará por qué no se puede cambiar el elemento de una tupla")

print('///////////////////////////////////')
#Mostramos como si podemos 'modificar' una tupla creando una nueva

nueva_tupla=(10, 'Hola', 3.5)

print('Nueva tupla con el primer elemento modificado,', nueva_tupla)
print('Tupla original permanece sin cambios:', tupla_mixta)


