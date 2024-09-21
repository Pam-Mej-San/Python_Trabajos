#lista inicial

mi_lista=[10,20,30,40,50]
print('Lista original', mi_lista)

#Actualizar un elemento en específico
mi_lista[2]=35
print('Lista después de actualizar el tercer elemento', mi_lista)

#Actualizar un elemento usando el índice negativo

mi_lista[-1]=60

print('Mi lista después de cambiar el último elemento', mi_lista)

#Actualizar varios elementos usando slicing
mi_lista[1:4]=[25,35,45]
print('La lista después de actualizar un rango de elementos', mi_lista)

for i in range(len(mi_lista)):
    if mi_lista [i]>30:
        mi_lista[i]+=10
print('La lista después de actualizar elementos mayores a 30', mi_lista)