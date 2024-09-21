# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
#• Crea una tupla llamada frutas con los siguientes elementos:
#("manzana", "banana", "cereza").
#• Usa el método index para encontrar la posición de la fruta "banana".
#• Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un
# mensaje indicando que no está presente

# Banana time
mi_tupla=('manzana', 'banana', 'cereza')
indice_banana=mi_tupla.index('banana')

print('El elemento banana se encuentra en la posición',indice_banana,' de la tupla')

#Naranja time
búsqueda='Naranja'

if búsqueda in mi_tupla:
    print('La variable', búsqueda,'se encuentra en la tupla' )
else:
    print('La variable', búsqueda ,'NO se encuentra en la tupla' )



