# Ejercicio Combinado
#Desarrolla un programa que:
#1. Genere una lista de números aleatorios entre 1 y 20.
#2. Usa un bucle for con range para iterar sobre la lista.
#3. Usar continue para saltar números menores de 10.
#4. Usar break para detener la iteración si se encuentra un número
#divisible por 15.
#5. Imprimir todos los números que cumplen las condiciones.
#6. Utilizar list comprehension para filtrar los números que no cumplen
#ninguna condición.

numeros = list(range(1, 21))

numeros_cumplen = []
for i in range(len(numeros)):
    numero = numeros[i]
    
    if numero < 10:
        continue
    
    if numero % 15 == 0:
        print(f"Número divisible por 15 encontrado{numero}")
        break 
#15
numeros_cumplen.append(numero)

#No cumplen
numeros_no_cumplen = [num
                     for num in numeros 
                     if num < 10 and num % 15 != 0]

print("Lista de números generados:", numeros)
print("Números que cumplen las condiciones:", numeros_cumplen)
print("Números que no cumplen ninguna condición:", numeros_no_cumplen)
