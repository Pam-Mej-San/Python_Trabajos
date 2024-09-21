#Ejercicio 1: Contador de Números Específicos
#Escribe un programa que cuente cuántas veces aparece un número
#específico en una lista.
##Instrucciones:
#• Define una lista de números predefinida o pídele al usuario que
#ingrese los números.
#  Pide al usuario que ingrese un número a buscar.
#• Usa el método count() para determinar cuántas veces aparece el
#número en la lista.
#• Muestra el resultado.8

mi_lista=[0,1,2,3,4,2,6,7,2,9,8,1,8]
buscador=int(input('Escribe el número que buscas:'))
conteo=mi_lista.count(buscador)
print(f'Tú numero se repite:',{conteo},'veces')
