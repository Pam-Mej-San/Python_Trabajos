#Suma de Sublistas
#Crea un programa que tome una lista de números y calcule la suma de una
#sublista especificada por el usuario.
#Instrucciones:
#• Define una lista de números predefinida.
#• Pide al usuario que ingrese el índice de inicio y el índice de fin para
#la sublista.
#• Usa slicing para obtener la sublista.
#• Suma los elementos de la sublista
# Muestra la suma.

mi_lista=[1,2,3,4,5,6,7,8,9,10]
print('La lista original es:', mi_lista)

sublista_a=(int(input('Ingresa el inicio tu sublista: ')))
sublista_b=(int(input('Ingresa el final de tu sublista: ')))

sublista= mi_lista[sublista_a:sublista_b+1]
final=sum(sublista)

print('Sublista', sublista)
print('La suma final de todos los números de la lista es:', {final})


