#Lista vacía

#La longitud de una lista vacía

lista_vacía=[]
print('Longitud de una lista vacía',len(lista_vacía))

#lista con enteros
#La longitud de una lista es igual al número de elementos de una lista

lista_enteros=[1,2,3,4,5]
print('La longitud e una lista de enteros es de:', len(lista_enteros))


#Lista con cadenas
#La longitud es igual al número de elementos de la lista

lista_cadenas=['Manzana', 'Piña', 'Fresa']
print('Longitud de una lista de cadenas es de:', len(lista_cadenas))

#Lista mixta
#La longitud cuenta todos los elementos (sin importar el tipo de elemento)

lista_mixta=[1,'Text a', 3, 'Text b',5,[1,2,'text',3,4]]

print('La longitud de la lista mixta es:', len(lista_mixta))

#Lista de elementos compartidos.
#La longitud es el resultado de multiplicar el número de elementos repetidos

lista_repeat=[0]*10
print('La longitud de la lista de números repetidos es:', len(lista_repeat))


