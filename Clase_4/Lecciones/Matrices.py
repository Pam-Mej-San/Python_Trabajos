#Definir una matriz de 3 x 3

matriz=[
    [1,2,3], #FILA 0
    [4,5,6], #FILA 1
    [7,8,9] #FILA 2
    ]

#Acceder y mostrar algunos elementos específicos

print('Algunos elementos de la matriz')
print('Algunos elementos de la fila 0:', matriz[0][0])
print('Elementos en la fila 1 columna 2', matriz [1][2])

#Modificar elementos específicos
print('\n Modificar elementos de la Matriz')

matriz [0][1]=10
matriz [2][0]=15

print('Matriz después de las modificaciones')
print(matriz)

#Acceder a la fila completa

print('\n Acceder a la fila completa')
fila_completa= matriz[1] #obtener toda la fila
print('Fila completa en la posición 1', fila_completa)

#Reemplazar una fila completa

print('\n Reemplazar a la fila completa')
matriz[1]=[20,21,22]
print('Matriz des pués de remplazar la fila 1',matriz)


#Trabajar con una submatriz (parte de una matriz)

submatriz= [matriz [0][1:3]], matriz [1][1:3]
print('Submatriz extraída:', submatriz)

#Mostr'amos toda la matriz al final
print('\n Matriz completa')
print(matriz[0])
print(matriz[1])
print(matriz[2])


