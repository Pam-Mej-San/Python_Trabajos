#Ejercicio 1: Calificación con Operador Ternario
#Escribe un programa que asigna un mensaje a una variable resultado
# basado en una calificación (entre 0 y 100). Usa el operador ternario
# para asignar "Aprobado" si la calificación es mayor o igual a 60 y
#"Reprobado" en caso contrario.

Cal=float(input('introduce tu calificación:'))

if Cal==100 or Cal>60:
    mensaje='Aprobada'
else:
    mensaje='Reprobada'

print(mensaje)
