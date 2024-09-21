#Crea un programa que reciba una lista de números y realice las siguientes
#operaciones:
#1. Crear un set a partir de la lista para eliminar duplicados.
#2. Iterar sobre el set e imprimir cada número.
#3. Contar cuántos números son mayores que un valor dado y
#almacenarlos en un nuevo set

lista_a={1,2,3}
lista_b={3,4,5}
lista_c={5,6,7}

#Eliminar duplicados
lista_completa=lista_a | lista_b | lista_c
print('Esta es la lista completa sin duplicados:', lista_completa)

print('Impresión de cada número en la lista:')
for numero in lista_completa:
    print(numero)

#Mayor que
valor=5
otros_num=[]
for numero in lista_completa:
    if numero > valor:
        otros_num.append(numero)

print('Números mayores que', valor,':',otros_num)

contar=len(otros_num)
print('Cantidad de números mayores que',valor,':',contar)


