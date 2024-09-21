#Ejercicio de Sets y Operaciones Básicas
#Escribe un programa que:
#1. Cree dos sets de números.
#2. Realice operaciones de unión, intersección y diferencia entre estossets.
#3. Imprima los resultados de cada operación.


set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}

union_set = set_1.union(set_2) 
interseccion_set = set_1.intersection(set_2) 
diferencia_set = set_1.difference(set_2)  

print("Set 1:", set_1)
print("Set 2:", set_2)
print("Unión de set_1 y set_2:", union_set)
print("Intersección de set_1 y set_2:", interseccion_set)
print("Diferencia entre set_1 y set_2:", diferencia_set)
