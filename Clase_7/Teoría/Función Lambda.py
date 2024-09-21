#Función Lambda

suma=lambda x,y: x+y
print(f'Suma de 5 y 3: {suma(5,3)} ')

#Usando map()
numeros=[1,2,3,4,5]
cuadrados = map (lambda x:x **2, numeros)
print(f'Cuadrados de la lista: {numeros}: {list (cuadrados)}')

#Usando filter ()
numeros2=[1,2,3,4,5,6]
pares=filter(lambda x: x%2==0, numeros)
print(f'Números pares en: {numeros2}:{list(pares)}')

#Usando sorted ()
tuplas=[(1,2),(3,4),(5,0)]
ordenadas=sorted(tuplas, key=lambda t:t [1])
print(f'Lista de tuplas ordenadas por el segundo elemento:{ordenadas}')

#Usando reduce ()
from functools import reduce
numeros= [1,2,3,4]
producto=reduce(lambda x,y:x*y, numeros)
print(f'Producto de todos los elementos en {numeros}: {producto}')

# Ejemplo 6: Uso de Lambda con funciones personalizadas
resta = lambda x, y: x - y
print (f"Resta de 10 - 7: {resta(10, 7)}") # Imprime 3


# Ejemplo 7: so de Lambda en funciones integradas (sorted con strings)
nombres = ['Ana', 'Carlos', 'Beatriz', 'David']
ordenados = sorted (nombres, key=lambda nombre: len (nombre))
print (f"Nombres ordenados por longitud: {ordenados}") # Imprime ['Ana', 'David", 'Carlos", 'Beatriz']

