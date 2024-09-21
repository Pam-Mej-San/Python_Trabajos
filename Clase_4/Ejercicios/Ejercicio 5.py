#Ejercicio 5: Manejo de Matrículas en una Tupla
#• Crea una tupla llamada matriculas con los siguientes números de
#matrícula: (101, 102, 103, 104, 105).
#• Usa el método count para contar cuántas veces aparece el número
#de matrícula 102 en la tupla.
#• Usa el método index para encontrar la posición del número de
#matrícula 104 en la tupla.

mi_tupla=(101, 102, 103, 104, 105)

#COUNT
búsqueda=mi_tupla.count(102)
print('El número 120 aparece',búsqueda,'vez/veces')

#INDEX
índice=mi_tupla.index(104)
print('El número 104 se encuentra en la posición', índice, 'de la tupla')




