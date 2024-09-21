#Crear una matriz 3x3 usando listas dentro de listas
matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#Imprimir la matriz completa
print('Matriz:')
for fila in matriz:
    print(fila)

#Acceder al elemento en la segunda fila, tercera columna
elemento = matriz [1][2] # Fila 1 (Segunda fila), Columna 2 (Tercera columna)
print('\n Elemento en la segunda fila, tercera columna:', elemento)

#Acceder a otro elemento, por ejemplo el primer elemento de la tercera fila
otro_elemento= matriz [2][0] #Fila 2 (tercera fila), Columna 0 (primera columna)
print('Elemento en la tercera fila, primera columna:', otro_elemento) #Output:7