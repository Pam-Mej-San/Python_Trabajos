#Crear un diccionario que representa a un estudiante
estudiante = {
    'Nombre': 'Laura',
    'Edad' : 20,
    'Calificaciones': [85, 92, 78, 90]
}

#Imprimir el diccionario completo
print('Diccionario del estudiante:')
print(estudiante)

#Acceder a la lista de calificaciones
calificaciones= estudiante ['Calificaciones']
print('\n Calificaciones:', calificaciones)

#Acceder a una calificación específica, por ejemplo, la segunda calificación
segunda_calificacion= calificaciones[1]
print('\nSegunda calificación:', segunda_calificacion) #Output 92

#Añadir una nueva calificación a la lista
estudiante['Calificaciones'].append(88)
print('\n Calificaciones actualizadas', estudiante ['Calificaciones'])

print('////////////////////////////')