#
# Ejercicio de while con Condiciones y Contadores
#Desarrolla un programa que:
#1. Use un bucle while para generar números de la serie de Fibonacci.
#2. Continúe generando números hasta que el número actual sea mayor
#o igual a 100.
#3. Imprima la serie de Fibonacci generada.
#

a, b = 0, 1

fibonacci = []

while a < 100:
    fibonacci.append(a)
    
    a, b = b, a + b

print("Serie de Fibonacci generada:", fibonacci)
