numeros = list(range(1, 10))
print(numeros) 

#Cuadrados imparaes

cuadrados_impares = [numero ** 2 for numero in numeros if numero % 2 != 0]
print(cuadrados_impares) 