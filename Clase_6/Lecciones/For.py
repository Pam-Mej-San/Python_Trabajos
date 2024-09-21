#Programa para imprimir cuadrados de numeros y calcular la suma
# Lista de numeros
numeros = [1, 2, 3, 4, 51]
#iniciamos variable
suma_cuadrados = 0
#iterar sobre cada numero en la lista
for numero in numeros:
    #calcular el cuadrado del numero
    cuadrado = numero ** 2
    #Imprimir el cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    #agregar el cuadrado a la suma suma_cuadrados += cuadrado
#Imprimir
print(f"La suma de los cuadrados es: {suma_cuadrados}")