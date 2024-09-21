#Ejercicio de List Comprehension y range
#Crea un programa que:
#1. Use range para generar una lista de números del 1 al 15.
#2. Utilice list comprehension para crear una nueva lista con el cubo
#de los números pares
#



numeros = list(range(1, 16))

cubosypares = [numero ** 3 for numero in numeros if numero % 2 == 0]

print("La lista de números del 1 al 15 es:", numeros)
print("Los Cubos de los números pares:", cubosypares)


